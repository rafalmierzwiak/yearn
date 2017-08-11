package main

import (
	"fmt"
    "io"
    "io/ioutil"
    "html/template"
	"log"
	"net/http"
    "os"
)

const templatesPath string = "trackMyRequests"
const serviceStatusPath string = "trackMyRequests/serviceStatus"
const serviceImagePath string = "trackMyRequests/serviceImage"
const serviceImageUrl string = "https://logo.clearbit.com/sojern.com"

type StatusPage struct {
    Body  []byte
}

func (p *StatusPage) save() error {
    return ioutil.WriteFile(serviceStatusPath, p.Body, 0600)
}

func loadStatusPage() (*StatusPage, error) {
    body, err := ioutil.ReadFile(serviceStatusPath)
    if err != nil {
        return nil, err
    }
    return &StatusPage{Body: body}, nil
}

func renderTemplate(w http.ResponseWriter, tmpl string, p *StatusPage) {
    t, err := template.ParseFiles(templatesPath + "/" + tmpl + ".html")
    if err != nil {
        log.Fatal(err)
    }
    t.Execute(w, p)
}

func editStatusHandler(w http.ResponseWriter, r *http.Request) {
    p, err := loadStatusPage()
    if err != nil {
        p = &StatusPage{}
    }
    renderTemplate(w, "edit", p)
}

func saveStatusHandler(w http.ResponseWriter, r *http.Request) {
    body := r.FormValue("body")
    p := &StatusPage{Body: []byte(body)}
    p.save()
    http.Redirect(w, r, "/viewStatus", http.StatusFound)
}

func viewStatusHandler(w http.ResponseWriter, r *http.Request) {
    p, _ := loadStatusPage()
    renderTemplate(w, "view", p)
}

func imageHandler(w http.ResponseWriter, r *http.Request) {
    if _, err := os.Stat(serviceImagePath); err == nil {
  	  http.ServeFile(w, r, serviceImagePath)
    }
}

func statusHandler(w http.ResponseWriter, r *http.Request) {
    fi, err := os.Stat(serviceStatusPath)

    if err != nil {
        fmt.Fprintf(w, "Error 503 (Service not available)")
        return
    }

    if fi.Size() == 0 {
        fmt.Fprintf(w, "OK")
    } else {
        http.ServeFile(w, r, serviceStatusPath)
    }
}

func fetchServiceImage() {
    fi, err := os.Stat(serviceStatusPath)

    if err == nil && fi.Size() > 0 {
        return
    }

    response, err := http.Get(serviceImageUrl)
    if err != nil {
        log.Fatal(err)
    }

    defer response.Body.Close()

    serviceImageFile, err := os.Create(serviceImagePath)
    if err != nil {
        log.Fatal(err)
    }

    _, err = io.Copy(serviceImageFile, response.Body)
    if err != nil {
        log.Fatal(err)
    }

    serviceImageFile.Close()
}

func main() {

    fetchServiceImage()

	http.HandleFunc("/serve", imageHandler)
	http.HandleFunc("/status", statusHandler)

    http.HandleFunc("/editStatus", editStatusHandler)
    http.HandleFunc("/saveStatus", saveStatusHandler)
    http.HandleFunc("/viewStatus", viewStatusHandler)

	log.Fatal(http.ListenAndServe(":8080", nil))

}

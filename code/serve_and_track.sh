#!/bin/bash

cmd_name="$(basename $0)"

server_log_file="/tmp/server.log"
service_image_file="/tmp/service_image"
service_image_url="https://logo.clearbit.com/sojern.com"
service_status_file="/tmp/service_status"


usage() {
    echo "Usage: ${cmd_name}"
    echo
    echo "A tiny wee webserver. Script starts socat (binds and listens to :8080)"
    echo "and re-launches itself in worker mode upon client connection."
    echo
    echo "  /image  - will serve image /tmp/service_image"
    echo "  /status - will respond with HTTP 200 if /tmp/service_status exist"
    echo "                              HTTP 503 otherwise"
    echo "  (other) - will respond with 501 not implemented"
    echo
    exit 0
}


die() {
    echo -e "$1"
    exit 1
}


log() {
    local remote_host="$1"
    local request=$(echo "$2" | tr -d '\r')
    local response_code="$3"
    local datestamp=$(TZ=ETC/GMT date '+[%d/%b/%Y:%k:%M:%S %z]')

    echo -e "${remote_host} - - ${datestamp} \"${request}\" ${response_code}" >&2
}


init() {
    [[ -s "${service_image_file}" ]] \
        || wget -qO "${service_image_file}" "${service_image_url}" \
        || die "ERROR: Unable to download service image"
}


main() {
    [[ "$(ps -o comm ${PPID})" =~ "socat" ]] \
        && worker \
        || server
}


server() {
    socat \
        TCP4-LISTEN:8080,reuseaddr,keepalive,keepintvl=1,keepcnt=2,fork \
        "SYSTEM: SOCAT_PEERADDR=\${SOCAT_PEERADDR} ./${cmd_name}"
}


worker() {
    while read http_request; do
        if [[ "${http_request}" =~ ^GET ]]; then
            if [[ "${http_request}" =~ "/ping " ]]; then
                http_response_code=200
                response_status
            elif [[ "${http_request}" =~ "/img " ]]; then
                http_response_code=200
                response_image
            else
                http_response_code=501
                response_not_implemented
            fi
            log "${SOCAT_PEERADDR}" "${http_request}" "${http_response_code}"
            exit
        fi
    done
}

response_image() {
    echo -en "HTTP/1.1 200\r\n"
    echo -en "Content-Type $(file -b --mime-type ${service_image_file})\r\n"
    echo -en "Connection: close\r\n"
    echo -en "\r\n"
    cat "${service_image_file}"
}


response_not_implemented() {
    echo -en "HTTP/1.1 501\r\n"
    echo -en "Content-Type: text/html; charset=UTF-8\r\n"
    echo -en "Connection: close\r\n"
    echo -en "\r\n"
    echo -en "ERROR 501 (Not implemented)"
    echo -en "\r\n"
}


response_status() {
    [[ -f "${service_status_file}" ]] \
        && http_response_code="200" \
        || http_response_code="503"

    echo -en "HTTP/1.1 ${http_response_code}\r\n"
    echo -en "Content-Type: text/html; charset=UTF-8\r\n"
    echo -en "Connection: close\r\n"
    echo -en "\r\n"

    [[ "${http_response_code}" == "200" ]] \
        && echo -en "$(cat ${service_status_file})\r\n" \
        || echo -en "ERROR 503 (Service not available)"
}

[[ "$1" == "--help" ]] \
    && usage

init
main "$@"

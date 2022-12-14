use std::{
    fs,
    io::{prelude::*, BufReader, Write},
    net::{TcpListener, TcpStream},
};

fn main() {
    std::io::stdout().write("All hail the crab.".as_bytes()).unwrap();
    //print!("{}", fs::read_to_string("hello.html").unwrap());
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let request_line = buf_reader
        .lines()
        .next()
        .unwrap()
        .unwrap();

    println!("{}", request_line);

    if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();
        let response = format!(
            "{status_line}\r\n\
Content-Length: {length}\r\n\r\n\
{contents}"
        );
        stream.write_all(response.as_bytes()).unwrap();
        } else {
        //print!("hello");
        let status_line = "HTTP/1.1 404 NOT FOUND";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();
        let response = format!(
            "{status_line}\r\n\
Content-Length: {length}\r\n\r\n
{contents}"
        );
        stream.write_all(response.as_bytes()).unwrap();
    }
}
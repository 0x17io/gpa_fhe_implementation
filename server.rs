use std::{
    //fs,
    io::{prelude::*, BufReader, Write},
    net::{TcpListener, TcpStream},
};

fn main() {
    std::io::stdout().write("All hail the crab.\n".as_bytes()).unwrap();
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

    let response = format!("hi from the server");
    stream.write_all(response.as_bytes()).unwrap();
}

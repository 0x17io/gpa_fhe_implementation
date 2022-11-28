use std::io::prelude::*;
use std::io::Result;
use std::net::TcpListener;
use std::net::TcpStream;

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 512];
    stream.read(&mut buffer).unwrap();
    let mut incoming_data = String::from_utf8_lossy(&buffer[..]);
    let data_to_process = incoming_data.trim_matches(char::from(0));
    println!("{}", data_to_process);
    let response = format!("hi from the server");
    
    stream.write_all(response.as_bytes()).unwrap();
}

pub fn create_listener(addr: String) -> Result<()> {
    let listener = TcpListener::bind(addr)?;
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        handle_connection(stream);
    }
    Ok(())

}


fn main() -> Result<()> {
    create_listener(String::from("127.0.0.1:7878"))
}

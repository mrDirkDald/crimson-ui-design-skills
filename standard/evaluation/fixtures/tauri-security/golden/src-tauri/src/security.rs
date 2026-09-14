pub fn validate_path(path:&std::path::Path, root:&std::path::Path)->bool { match path.canonicalize(){ Ok(p)=>p.starts_with(root), Err(_)=>false } }

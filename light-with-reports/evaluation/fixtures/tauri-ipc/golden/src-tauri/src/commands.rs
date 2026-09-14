#[derive(serde::Serialize)] struct TaskSnapshot { task_id:String, state:String }
#[tauri::command] async fn start()->Result<TaskSnapshot,String>{ todo!() }
#[tauri::command] async fn cancel(task_id:String)->Result<TaskSnapshot,String>{ todo!() }
#[tauri::command] async fn query_tasks()->Result<Vec<TaskSnapshot>,String>{ todo!() }

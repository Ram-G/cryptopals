pub fn get_result_message(succeeded: bool) -> String {
    return if succeeded { "Success".to_string() } else { "Failed".to_string() };
}

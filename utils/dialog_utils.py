def handle_dialog(page, action_to_trigger_dialog, timeout=5000):
    with page.expect_event("dialog", timeout=timeout) as dialog_info:
        action_to_trigger_dialog()
    dialog = dialog_info.value
    alert_text = dialog.message
    dialog.accept()
    return alert_text

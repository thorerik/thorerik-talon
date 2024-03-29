mode: dictation
experiment: anchor-file
-

# Freely dictate text
<user.prose>:   auto_insert(prose)

(new line | ny linje):
    edit.line_insert_down()
    user.dictation_format_reset()

(comma | komma): ","
(punctuation | punkt): "."


# Switch to command mode and insert a phrase
(command mode | over | ende) [<phrase>]$:
    user.command_mode(phrase or "")

# Insert the actual words
escape words <user.words>$:
    auto_insert(words)
escape words <user.words> over:
    auto_insert(words)
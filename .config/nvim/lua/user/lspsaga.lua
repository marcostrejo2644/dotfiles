local status_ok, saga = pcall(require, "lspsaga")
if not status_ok then
  return
end

-- Error,Warn,Info,Hint
local diagnostic_header_icon = {' ',' ',' ','ﴞ '}
-- use emoji lightbulb in default
local code_action_icon = '💡'
-- if true can press number to execute the codeaction in codeaction window
local code_action_num_shortcut = true
-- same as nvim-lightbulb but async
local code_action_lightbulb = {
  enable = true,
  sign = true,
  sign_priority = 20,
  virtual_text = true,
}
local finder_definition_icon = '  '
finder_reference_icon = '  '
max_preview_lines = 10 -- preview lines of lsp_finder and definition preview
finder_action_keys = {
  open = 'o', vsplit = 's',split = 'i',quit = 'q',scroll_down = '<C-f>', scroll_up = '<C-b>' -- quit can be a table
}
code_action_keys = {
  quit = 'q',exec = '<CR>'
}
rename_action_keys = {
  quit = '<C-c>',exec = '<CR>'  -- quit can be a table
}
-- definition_preview_icon = '  '
-- "single" "double" "round" "plus"
border_style = "single"
rename_prompt_prefix = '➤'
saga.setup()

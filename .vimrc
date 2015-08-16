" Init file 


"VIM history

set history=100

"Word wrap

set wrap
set linebreak 
set nolist

"View line numbers

set number

"Ignore case when searching 

set ignorecase 

"Status line

set laststatus=2

"set statusline=%F%7l%7m

set statusline=
set statusline +=%1*\ %n\ %*		"buffer number
set statusline +=%5*%{&ff}%*            "file format
set statusline +=%3*%y%*                "file type
set statusline +=%4*\ %<%F%*            "full path
set statusline +=%2*%m%*                "modified flag
set statusline +=%1*%=%5l%*             "current line
set statusline +=%2*/%L%*               "total lines








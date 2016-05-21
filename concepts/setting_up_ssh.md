## Setting up SSH

create an ssh key for the second account

`ssh-keygen -t rsa -C "your_email@youremail.com"`

when prompted, make sure you name the file something other than the default

`"Enter file in which to save the key (/Users/you/.ssh/id_rsa): /Users/you/.ssh/id_rsa2`

add the second key to the ssh agent

`ssh-add ~/.ssh/id_rsa2`

copy public key to the clipboard

`pbcopy < ~/.ssh/id_rsa2.pub`

add the second key to your Github account

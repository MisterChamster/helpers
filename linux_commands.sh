# List all boot options
sudo efibootmgr
sudo efibootmgr -v

# Change boot order
sudo efibootmgr -o 0006,0000

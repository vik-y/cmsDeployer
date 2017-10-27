# cmsDeployer
Deploy wordpress websites within seconds. Presently this focuses only on WordPress but later on it can support other CMS too.  

# What does this do?
You can instantly provision wordpress websites using this. Just install it on your server and make sure that the domain's A records
point to your server. And that's it. You can deploy as many wordpress sites as you want. 

For example if you want to create 3 wordpress sites on your server. Each of them are site1, site2 and site3. You want them 
to be accessible at the following links: 

 - site1.example.com
 - site2.example.com
 - site3.example.com 

After installation you can just run 
```sh
python create_site.py site1 site1.example.com 
python create_site.py site1 site2.example.com 
python create_site.py site1 site3.example.com 
```
And that's it, you are done! All 3 wordpress websites are online now. 
NOTE: The A record of site1.example.com, site2.example.com and site3.example.com should point to your server's IP Address.

# Installation
```sh
# Run the commands written below one by one. Don't copy paste all at once. 
git clone https://github.com/vik-y/cmsDeployer
cd cmsDeployer 
./install.sh
./init.sh 
```
If you don't get any error then your installation is done. *Exit your current terminal session and login again*. If you are using
Ubuntu Desktop then you might have to logout and login. 

To check if installation succeeded `docker run hello-world` should not give any error. 

# TODO: 
 * Add support for CMS other than wordpress. .
 * Add support for different Databases 


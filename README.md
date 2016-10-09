Local machine Set up Instruction 

Pull all the most recent changes 
use the command "git pull --rebase" 

set up virtual environment to manage dependency

//First install pip
sudo easy_install pip

//Install virtual environment in the repository directory inside of the Jedi_Project directory
sudo pip install virtualenv

//Activate the virtual environment
source env/bin/activate

//Install all the dependency packages
sudo pip install -r dependency.txt

//Install Flask
sudo pip install Flask

//go to Jedi_Project directory 
cd /Jedi_Project

//run Webservice
python app.py


go to the browser and type url
localhost:5710/test

# Installation/Setup
#### Creating the Bot to use
- Go to the [Discord Developer Portal](discord.com/developers/applications) and make a Application,
- Enable the bot flag in the application settings,
- Add your bot token to line 30, 
- Add the bot to your server, 
#### Running the program
- Clone the Repository(`git clone https://github.com/thesillyboi/ServerStatus`)
- Run the program(``python main.py``) or make a build of it using [uv](https://docs.astral.sh/uv/) and run that (`uv build`)


>If it always says it's offline, change line 10 to be the name of the server process, I just made an educated guess on what the process would be called, but it could very  likely be incorrect


>*If you have an issue with running it, make sure you're in the venv(Also known as a  Virtual Environment), or make a new venv and add discord and psutil to dependencies(or in one shell script, `` uv venv && source.venv/bin/activate && uv pip install discord psutil `` )*

### This was written on a whim, if you want more added, please put them in a GitHub issue or do them yourself in a pull request.
*I have no major plans to continue work on this, this was just meant to fix an annoyance with me never knowing when Modcraft is online, you could always put it on a timer or something else*

  This was made by Adrian Tennies for Modcraft, but for any other server of any kind to use it would be great ✌️ 
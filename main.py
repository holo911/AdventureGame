from flask import Flask, render_template, request

# PYTHON SCRIPT - LUCAS BUBNER

# -- DEMONSTRATES SKILLS OF --
# IF ELSE AND ELIF STATEMENTS
# GLOBAL BOOLEAN AND VARIABLES
# APP ROUTE DECORATOR
# PYTHON SYNTAX AND INDENTURE
# PYTHON LISTS
# BASIC USAGE OF FLASK LIBRARY

# -- ADDITIONAL SKILLS --
# JAVASCRIPT FRONTEND, UTILISING JQUERY LIBRARY
# HTML + CSS FRONTEND WEBSITE CONSTRUCTION
# FILE MANAGEMENT

app = Flask(__name__)
# name to name_error just incase the player skips the index page
name = "name_error"
namecap = "NAME_ERROR"

# Create empty array (list, but im going to call it an array because literally every other language calls it an array) for items we're carrying, used in the xC saga
# We could use simple boolean for this, but this is simply to expand Python knowledge
items = []

# Make new global boolean for the things we do (call mum, sleep early, play new game etc.)
imRude = False
Tired = False
newGame = False
tvSleep = False
lateNightChips = False

# xC pathway boolean


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', )


@app.route('/endings', methods=['GET'])
def endings():
    return render_template('endings.html', )


@app.route('/story', methods=['GET'])
def story():
    global name
    global namecap
    name = request.args.get("playername")
    # Capitalise the first letter of their name
    name = name.capitalize()
    # Create a fullcaps varient
    namecap = name.upper()
    return render_template(
        'intro.html',
        NAME=name,
    )


@app.route('/storyrestart', methods=['GET'])
def storyrestart():
    global name
    # As the code has not been reloaded, we need to set every variable back to False, while passing name through to restart
    global imRude, Tired, newGame, tvSleep, lateNightChips
    imRude = Tired = newGame = tvSleep = lateNightChips = False
    return render_template(
        'intro.html',
        NAME=name,
    )


@app.route('/startgame', methods=['GET'])
def startgame():
    global name
    return render_template(
        'xBase.html',
        NAME=name,
    )


@app.route('/chips', methods=['GET'])
def chips():
    global name
    return render_template(
        'xC.html',
        NAME=name,
    )


@app.route('/tv', methods=['GET'])
def tv():
    global name
    return render_template(
        'xTV.html',
        NAME=name,
    )


@app.route('/bed', methods=['GET'])
def bed():
    global name
    return render_template(
        'xC-Bed.html',
        NAME=name,
    )


@app.route('/cleanteeth', methods=['GET'])
def cleanteeth():
    global name
    return render_template(
        'xC-Teeth.html',
        NAME=name,
    )


@app.route('/mum', methods=['GET'])
def mum():
    global name
    global imRude
    imRude = False  # Resetting to False because of back key messing up variables
    return render_template(
        'xTV-Mum.html',
        NAME=name,
    )


@app.route('/standforever', methods=['GET'])
def standforever():
    global name
    global lateNightChips

    if lateNightChips == True:
      pageBuffer = 'ENDING-ChipFinder.html'
    else:
      pageBuffer = 'ENDING-StandForever.html'
  
    return render_template(
        pageBuffer,
        NAME=name,
    )

@app.route('/standforevermum', methods=['GET'])
def standforevermum():
    global name
    return render_template(
        'ENDING-StandForeverMum.html',
        NAME=name,
    )

@app.route('/berude', methods=['GET'])
def berude():
    global name
    global imRude
    imRude = True
    return render_template(
        'xTV-Ignore.html',
        NAME=name,
    )


@app.route('/sleep', methods=['GET'])
def sleep():
    global name
    global Tired
    Tired = False

    return render_template(
        'xTV-Mum-Sleep.html',
        NAME=name,
    )


@app.route('/chipstv', methods=['GET'])
def chipstv():
    global name
    global Tired
    global imRude
    global tvSleep
    tvSleep = True

    if imRude == True:
        Tired = True
        pageBuffer = 'xTV-ChipsDecide.html'
    else:
        pageBuffer = 'xTV-WatchTVChipsMum.html'

    return render_template(
        pageBuffer,
        NAME=name,
    )


@app.route('/gaming', methods=['GET'])
def gaming():
    global name
    global imRude
    global Tired

    if imRude == True:
        Tired = True

    return render_template(
        'xTV-GamingBridge.html',
        NAME=name,
    )


@app.route('/takeoutchips', methods=['GET'])
def takeoutchips():
    global name
    global Tired

    if Tired == True:
        pageBuffer = 'ENDING-TiredTakeOutChips.html'
    else:
        pageBuffer = 'ENDING-NotTiredTakeOutChips.html'

    return render_template(
        pageBuffer,
        NAME=name,
    )


@app.route('/bringoutchips', methods=['GET'])
def bringoutchips():
    global name
    return render_template(
        'ENDING-EnthusiasticTakeOutChips.html',
        NAME=name,
    )


@app.route('/gamedontknow', methods=['GET'])
def gamedontknow():
    global name
    global imRude

    if imRude == True:
        pageBuffer = 'xTV-PlayOGameFallAsleep.html'
    else:
        pageBuffer = 'xTV-PlayOGameMum.html'

    return render_template(
        pageBuffer,
        NAME=name,
    )


@app.route('/newgame', methods=['GET'])
def newgame():
    global name
    global imRude
    global newGame
    newGame = True

    if imRude == True:
        pageBuffer = 'xTV-PlayNGameFallAsleep.html'
    else:
        pageBuffer = 'xTV-PlayNGameMum.html'

    return render_template(
        pageBuffer,
        NAME=name,
    )


@app.route('/lie', methods=['GET'])
def lie():
    global name
    global imRude
    global newGame
    global tvSleep
    global lateNightChips

    if tvSleep == False and newGame == True:
        pageBuffer = '/'
    elif tvSleep == False and newGame == False:
        pageBuffer = '/'
    elif tvSleep == True and lateNightChips == False:
        pageBuffer = 'xTV-Mum-RushTV.html'
    elif tvSleep == True and lateNightChips == True:
        pageBuffer = 'xTV-Mum-RushTVAte.html'

    return render_template(
        pageBuffer,
        NAME=name,
    )


@app.route('/truth', methods=['GET'])
def truth():
    global name
    return render_template(
        'ENDING-MadMum.html',
        NAME=name,
    )


@app.route('/givechipseveryone', methods=['GET'])
def givechipseveryone():
    global name
    return render_template(
        'ENDING-ChipsGenocide.html',
        NAME=name,
    )


@app.route('/dietician', methods=['GET'])
def dietician():
    global name
    global tvSleep
    global imRude
    tvSleep = True

    if imRude == True:
        pageBuffer = 'xTV-WatchTVChipsFallAsleep.html'
    else:
        pageBuffer = 'xTV-WatchTVChipsMum.html'

    return render_template(
        pageBuffer,
        NAME=name,
    )


@app.route('/fatty', methods=['GET'])
def fatty():
    global name
    global lateNightChips
    global imRude
    global tvSleep
    lateNightChips = True
    tvSleep = True

    if imRude == True:
        pageBuffer = 'xTV-WatchTVChipsFallAsleepAte.html'
    else:
        pageBuffer = 'xTV-WatchTVChipsMum.html'

    return render_template(
        pageBuffer,
        NAME=name,
    )


@app.route('/taketime', methods=['GET'])
def taketime():
    global name
    return render_template(
        'ENDING-MadMumDeliquent.html',
        NAME=name,
    )


@app.route('/rush', methods=['GET'])
def rush():
    global name
    return render_template(
        'xTV-DoAnythingFallAsleepBridge.html',
        NAME=name,
    )


@app.route('/newgametalk', methods=['GET'])
def newgametalk():
    global name
    global Tired

    if Tired == True:
        pageBuffer = 'ENDING-FSNewGame.html'
    else:
        pageBuffer = 'ENDING-MumNewGame.html'

    return render_template(
        pageBuffer,
        NAME=name,
    )


@app.route('/oldgametalk', methods=['GET'])
def oldgametalk():
    global name
    global Tired
    global namecap

    if Tired == True:
        pageBuffer = 'ENDING-FSOldGame.html'
    else:
        pageBuffer = 'ENDING-MumOldGame.html'

    return render_template(
        pageBuffer,
        NAME=name,
        NAMECAP=namecap,
    )


@app.route('/takeoutdrone', methods=['GET'])
def takeoutdrone():
    global name
    return render_template(
        'ENDING-TakeOutDrone.html',
        NAME=name,
    )

@app.route('/computerinvestigate', methods=['GET'])
def computerinvestigate():
    global name
    return render_template(
        'ENDING-VistaMum.html',
        NAME=name,
    )

#@app.route('/', methods=['GET'])
#def ():
#  global name
#  return render_template(
#    '.html',
#    NAME = name,
#  )

if __name__ == "__main__":
    app.run(host='0.0.0.0')

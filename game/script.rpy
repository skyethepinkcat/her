# Declare characters used by this game.
define g = Character(_("A Voice"), color="c8ffc8")
define m = Character(_("You"), color="#ffabe9")
define v = Character(_("Val"), color="#cb59ff")
define b = Character(_("Friend"), color="#ffbb6f")
python:
  from enum import Enum

  class howLong(Enum):
    ELEMENTARY = 1
    MIDDLE = 2
    HIGH = 3
    COLLEGE = 4

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False
default tooWellKept = False
default wellKept = False
default wellKnown = False

default doneFriend = False
default doneEnemy = False
default doneSweet = False

default deadnameExplained = False

default relationshipFriend = 0
default relationshipSweetheart = 0
default relationshipEx = -10
default relationshipEnemy = -100

$ outLength = howLong.MIDDLE

# The game starts here.
label start:

scene bg

"Everything is still. There's not a breath of wind, not the motion of a small animal, not a flashing monitor or even the movement of time. You're not sure if anything exists."

"Really, you're not even sure if you exist. You don't remember how you got here. You don't remember anything."

show you at left
m "What is my name even?"

g "Now that certainly is the question, isn't it?"

m "Huh!? Wait, where did that- who's talking to me?"

g "This isn't about me, it's about you."

g "So? What's your name?"

menu:

  "You try to think..."

  "Layla":
    jump nameLayla
  "David":
    jump nameDavid
  "...":
    jump silence

label nameLayla:

  "That feels... right to you somehow."

  m "Layla, it's definetly Layla."

  g "What a cute name!"

  $wellKnown = True

  "[Without hestiation, you gave your true name. Your secret must have been *Well Known*.]"

  jump given

label nameDavid:

  "You cringe a bit, but you're pretty sure you know it."

  m "David... my name is David."

  g "Is that so?"

  m "Well..."

  g "Don't worry about it. I understand. Your name is Layla."

  "You weren't able to remember your true name. Your secret has been {b}Well Kept{/b} perhaps {b}Too Well Kept{/b}..."

  $wellKept = True
  $tooWellKept = True

  jump given

label silence:

  "You hesitate."

  g "I promise, you're safe here. Tell the truth."

  m "It's... Layla."

  g "Thank you for being honest with me Layla. You have a very cute name."
  "You hesitated before giving your true name. It was a {b}Well Kept{/b} secret."

  $wellKept = True

  jump given

label given:

m "So, what am I doing here? Who are you? Where... *is* here?"

g "That's not for me to decide. This is about you."

m "You've said that a few times now..."

g "Well, I suppose it's not only about you. It's also about the others."

m "Others?"

g "You tell me."

menu:

  "What does she mean by others..."

  "My Best Friend":
    jump friend

  "My Sweetheart":
    jump sweet

  "My worst enemy":
    jump enemy

label friend:

  m "Do you mean... my best friend?"

label sweet:

  if tooWellKept:

    m "Do you mean... him? That guy I met in college?"

    g "Hmm... Yes, but you're thinking of a girl I believe."

    m "Oh... Yeah that makes sense..."

    "You ponder for a moment."

    m "Am I... a girl?"

    g "Are you?"

    m "..."

    g "Only you can answer that."

    m "Yeah. I'm a girl."

    m "So, what was her name?"

    g "Val, she likes to be called."

    g "So... what do you remember?"

  else:

    m "Do you mean... her? That girl I met in college?"

    "You're not even sure how you remembered that detail."

    m "Val... I think her name was Val?"

    g "Go on..."

    $ length = ["error", "error"]

  if tooWellKept:

    $ length = ["short", "neck"]

  else:

    $ length = ["long", "waist"]

  "Around you, the white void begins to shape itself, color itself around you into something clearer. Street paths fade onto the ground, and a cloudy grass begins to emerge. In front of you, Val."

  show val at right

  "You know it's her before her features appear. Her [length[0]] golden hair is the first, slowly appearing on a blank head and falling to to her [length[1]]."

  v "Ah, I saw you in class didn't I? {i}Layla{/i} is it?"

  if wellKept:

    "She didn't say Layla, you remember that. But as she begins to say your deadname, there\'s the sound of a record scratch, and instead she says Layla."

    m "... What was that?"

    "Val, who's vague body had a moment ago been animated as any human, became suddenly rigid."

    if tooWellKept:

      g "This is all about you, Layla. She didn't have hair this long either. But that\'s how you think of it."

    else:
      g "This is all about you, Layla. That's how you think of this scene, so that's what you hear."

    m "I... that makes sense I suppose."

    "To put it simply, it does. It feels as intuitive as moving your hand."

    "Val begins to reanimate."

  if wellKept:
    m "Yeah, that's me. {i}Val{/i} right? What\'s up?"
  else:
    m "Yeah, that's me. Val right? What\'s up?"

  v "I was wondering if you could help me with..."

  menu:

    g "What did Val ask you to help her with?"

    "Math":
      v "...math, I was having trouble with integrals."

    "English":

      v "...english, I didn't really understand the poem we went over."

    "Chemistry":

      v "...chemistry, do you understand Stoiciometry?"

    "Makeup" if wellKnown:

      v "...makeup. Sorry if this is weird but I noticed your eyeliner. I suck at eyeliner, honestly!"

      m "Oh, sure thing. I'm not that though, honestly."

      menu:

        v "You say you aren't good, but look at yourself..."

        "My friend helped me, honestly.":

          v "Oh really?"

          "You must {b}still be friends{/b} with your Best Friend."

        "Thanks, I've had a lot of practice.":

          v "Ah, that's awesome!"

          "You've {b}been out for a while{/b}."

          if outLength > howLong.MIDDLE:
            $ outLength = howLong.MIDDLE






label enemy:


# # Start by playing some music.
# play music "illurock.opus"

# scene bg lecturehall
# with fade

# "It's only when I hear the sounds of shuffling feet and supplies being put away that I realize that the lecture's over."

# "Professor Eileen's lectures are usually interesting, but today I just couldn't concentrate on it."

# "I've had a lot of other thoughts on my mind...thoughts that culminate in a question."

# "It's a question that I've been meaning to ask a certain someone."

# scene bg uni
# with fade

# "When we come out of the university, I spot her right away."

# show sylvie green normal
# with dissolve

# "I've known Sylvie since we were kids. She's got a big heart and she's always been a good friend to me."

# "But recently... I've felt that I want something more."

# "More than just talking, more than just walking home together when our classes end."

# menu:

# "As soon as she catches my eye, I decide..."

# "To ask her right away.":

# jump rightaway

# "To ask her later.":

# jump later


# label rightaway:

# show sylvie green smile

# s "Hi there! How was class?"

# m "Good..."

# "I can't bring myself to admit that it all went in one ear and out the other."

# m "Are you going home now? Wanna walk back with me?"

# s "Sure!"

# scene bg meadow
# with fade

# "After a short while, we reach the meadows just outside the neighborhood where we both live."

# "It's a scenic view I've grown used to. Autumn is especially beautiful here."

# "When we were children, we played in these meadows a lot, so they're full of memories."

# m "Hey... Umm..."

# show sylvie green smile
# with dissolve

# "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

# "I'll ask her...!"

# m "Ummm... Will you..."

# m "Will you be my artist for a visual novel?"

# show sylvie green surprised

# "Silence."

# "She looks so shocked that I begin to fear the worst. But then..."

# show sylvie green smile

# menu:

# s "Sure, but what's a \"visual novel?\""

# "It's a videogame.":
# jump game

# "It's an interactive book.":
# jump book


# label game:

# m "It's a kind of videogame you can play on your computer or a console."

# m "Visual novels tell a story with pictures and music."

# m "Sometimes, you also get to make choices that affect the outcome of the story."

# s "So it's like those choose-your-adventure books?"

# m "Exactly! I've got lots of different ideas that I think would work."

# m "And I thought maybe you could help me...since I know how you like to draw."

# m "It'd be hard for me to make a visual novel alone."

# show sylvie green normal

# s "Well, sure! I can try. I just hope I don't disappoint you."

# m "You know you could never disappoint me, Sylvie."

# jump marry


# label book:

# $ book = True

# m "It's like an interactive book that you can read on a computer or a console."

# show sylvie green surprised

# s "Interactive?"

# m "You can make choices that lead to different events and endings in the story."

# s "So where does the \"visual\" part come in?"

# m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

# show sylvie green smile

# s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."

# m "That's great! So...would you be interested in working with me as an artist?"

# s "I'd love to!"

# jump marry

# label marry:

# scene black
# with dissolve

# "And so, we become a visual novel creating duo."

# scene bg club
# with dissolve

# "Over the years, we make lots of games and have a lot of fun making them."

# if book:

# "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

# "We take turns coming up with stories and characters and support each other to make some great games!"

# "And one day..."

# show sylvie blue normal
# with dissolve

# s "Hey..."

# m "Yes?"

# show sylvie blue giggle

# s "Will you marry me?"

# m "What? Where did this come from?"

# show sylvie blue surprised

# s "Come on, how long have we been dating?"

# m "A while..."

# show sylvie blue smile

# s "These last few years we've been making visual novels together, spending time together, helping each other..."

# s "I've gotten to know you and care about you better than anyone else. And I think the same goes for you, right?"

# m "Sylvie..."

# show sylvie blue giggle

# s "But I know you're the indecisive type. If I held back, who knows when you'd propose?"

# show sylvie blue normal

# s "So will you marry me?"

# m "Of course I will! I've actually been meaning to propose, honest!"

# s "I know, I know."

# m "I guess... I was too worried about timing. I wanted to ask the right question at the right time."

# show sylvie blue giggle

# s "You worry too much. If only this were a visual novel and I could pick an option to give you more courage!"

# scene black
# with dissolve

# "We get married shortly after that."

# "Our visual novel duo lives on even after we're married...and I try my best to be more decisive."

# "Together, we live happily ever after even now."

# "{b}Good Ending{/b}."

# return

# label later:

# "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."

# scene black
# with dissolve

# "But I'm an indecisive person."

# "I couldn't ask her that day and I end up never being able to ask her."

# "I guess I'll never know the answer to my question now..."

# "{b}Bad Ending{/b}."

# return

import asyncio
import discord
from discord.ext.commands import Bot
import os
import json
import time
import math
import random
from multiprocessing import Process
from discord.ext import tasks

async def timetest(reply):
    timeon = True
    time_person = message.author
    time_counter = 0
    channel = message.channel
    timer = True
    while timer:
        time_valid = True
        await P6(message)
        while time_valid:
            time_reply = await client.wait_for('message', check=None, timeout = None)
            if str(time_reply.author) == str(time_person):
                if time_reply.content.isdigit():
                    time_valid = False
            else:
                await message.channel.send("I only accept numbers")
        if int(time_reply.content) == int(answer):
            await message.channel.send("Correct!")
            counter += 1
        else:
            await message.channel.send("Too bad! The correct answer is {}".format(answer))



@tasks.loop(seconds=0)
async def countdown(message):
    global i
    global timer
    channel = message.channel
    time.sleep(1)
    i +=1
    print(i)
    if i == 5:
        timer = False
        timeon = False
        await message.channel.send("Time's up!")
    return i 
    pass 

async def P6(message):
    global y
    global x
    global answer
    global valid
    y = 0
    x = 1
    while (y < x) or y%x != 0:
        x = random.randint(3,19)
        y = random.randint(400,2000)
    operator = random.randint(1,4)
    if operator == 1:
        placement = random.randint(1,2)
        if placement == 1:
            await message.channel.send("What is {} * {}?".format(y,x))
            answer = y*x
        elif placement == 2:
            await message.channel.send("____ * {} = {}".format(x,x*y))
            answer = y
    elif operator == 2:
        await message.channel.send("What is {} / {}?".format(y,x))
        answer = y/x
        return answer
    elif operator == 3:
        x = 1
        y = 0
        while (y <= x) or y%x != 0:
            x = random.randint(4000,10000)
            y = random.randint(5000,20000)
        await message.channel.send("What is {} + {}?".format(y,x))
        answer = y+x
    elif operator == 4:
        x = 1
        y = 0
        while (y <= x) or y%x != 0:
            x = random.randint(4000,10000)
            y = random.randint(5000,20000)
        placement = random.randint(1,3)
        if placement == 1:           
            await message.channel.send("What is {} - {}?".format(y,x))
            answer = y-x 
        elif placement == 2:
            await message.channel.send("____ + {} = {}".format(x,x+y))
            answer = y
        elif placement == 3:
            await message.channel.send("{} + ____ = {}".format(y,x+y))
            answer = x
    valid = True

client = discord.Client()


async def on_message(message):
  if message.author == client.user:
    return 



    

@client.event
async def on_ready():
    global on
    global timeon
    print(f'{client.user} has connected to Discord!')
    on = False
    timeon = False




@client.event
async def on_message(message):
    global on
    global timeon
    kekw = client.get_emoji(int(836907284416167946))
    if not message.author.bot:
        if message.content.startswith("count"):
            if len(message.content.split()) > 1:
                number = int(message.content.split()[1])
            channel = message.channel
            for i in range(number):
                await channel.send(i+1)
        if message.content.startswith("why"):
            channel = message.channel
            name = str(message.author)
            await channel.send("why not @"+name)
        if message.content.startswith("$clear"):
            if len(message.content.split()) > 1:
                clear_number = int(message.content.split()[1])
                channel = message.channel
                await message.channel.purge(limit=clear_number+1)
        elif message.content.startswith('$send '):
            await message.channel.purge(limit=1)
            await message.channel.send(message.content[5:])
        if message.content.startswith('$mathtest') and on == False and timeon == False:
            print("1on",on)
            on = True
            person = message.author
            counter = 0
            channel = message.channel
            streak = True
            while streak:
                valid = True
                await P6(message)
                while valid == True:
                    reply = await client.wait_for('message', check=None, timeout = None)
                    print("on",on)
                    print("1",reply.author)
                    print("2",person)
                    print("3",message.content)
                    print("4",reply.content)
                    print(str(reply.author)==str(person))
                    print(reply.content.isdigit())
                    if str(reply.author) == str(person):
                        if reply.content.isdigit():
                            valid = False
                        else:
                            await message.channel.send("I only accept numbers")

                if int(reply.content) == int(answer):
                    await message.channel.send("Correct!")
                    counter += 1
                else:
                    await message.channel.send("Too bad! The correct answer is {}".format(answer))
                    await message.channel.send("Your final score is {}".format(counter))
                    if counter < 5:
                        await message.channel.send("Less than 5 points {}".format(kekw))
                    streak = False
                    on = False
        if message.content.startswith("$timetest") and timeon == False and on == False:
            i = 0
            countdown.start(message)
            timeon = True
            time_person = message.author
            time_counter = 0
            channel = message.channel
            timer = True
            while timer:
                time_valid = True
                await P6(message)
                while time_valid:
                    time_reply = await client.wait_for('message', check=None, timeout = None)
                    if str(time_reply.author) == str(time_person):
                        if time_reply.content.isdigit():
                            time_valid = False
                    else:
                        await message.channel.send("I only accept numbers")
                if int(time_reply.content) == int(answer):
                    await message.channel.send("Correct!")
                    counter += 1
                else:
                    await message.channel.send("Too bad! The correct answer is {}".format(answer))
            countdown.stop(message)















































































client.run('ODM1ODc4NDE4MTUwNDU3MzQ0.YIV2cA.gYY0hE0hLS_ho3gPIAmF90Y6gTQ')
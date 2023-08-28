# Challenge Details

Game reversing.

Godot game is exported to web. It loads the assets from a file that can be easily decompressed/decoded/decompiled(?) using an existing tool then loaded into Godot engine to view all the source code and level files.

But this would be too easy, so I obfuscated the JS code a bit and made it not so obvious.

# Setup Instructions

Host game web server
https://github.com/NUSGreyhats/greyctf23-challs/tree/daniel/re-metasize/final/re/metasize

# Key concepts

Game reverse engineering
Using existing tools
JS reverse engineering

# Solution

Realize it is a Godot game. Find out which one is the game asset file, decompile it, open in Godot engine, see the flag.

# Learning Objectives

Learn to consider that games are likely made with some game engine, so existing resources can be used to reverse them.
Learn that Godot games that aren't encrypted can be easily reversed and patched.

---

```
Hope you like this game.

The flag is hidden in one of the levels. You may need to cheat the game to walk through walls or fly around to find the flag.

Note: If you aren't sure whether the character is o or O or 0, they are all o
```

# Part 1

## Description

What game engine is used to make this game?

Flag format: Name of the game engine, all lowercase

## Hints 

1. Check the source files (html, css, js). Obviously, I have removed all traces of the game engine's name from the code. (Or did I?) You may also download every popular game engine, create a simple game project, export to HTML, and try to correlate the generated code with the one in this challenge.

## Flag

`godot`

# Part 2

## Description

Time to hack the game?

## Hints

1. There may be writeups online on Godot game reverse engineering that you may want to refer to.
2. If you can't find the pck file, consider the possibility that it was purposely renamed so that it's not so obvious.

## Flag

`grey{godot_hakor_2dcf839d}`

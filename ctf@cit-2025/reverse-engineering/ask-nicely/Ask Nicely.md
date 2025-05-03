# Ask Nicely - Writeup

| Author           | Title             | Category   | Difficulty |
|------------------|-------------------|------------|------------|
| barrythecanary | Ask Nicely | reverse engineering | - |

## Description

I made this program, you just have to ask really nicely for the flag!

## Attachment

[asknicely](./asknicely)

## Solution

Running the program on it's own looks the following:

```
$ ./asknicely 
How badly do you want the flag?
very
Ask nicely...
please
that's not quite what I'm lookng for.
```

Not sure if this was the intended solution but running strings and grep looking for "please" I found the following:

```
$ strings asknicely | grep 'please'
pretty pretty pretty pretty pretty please with sprinkles and a cherry on top
```

inputting that into the program gave me the flag.

```
$ ./asknicely 
How badly do you want the flag?

Ask nicely...
pretty pretty pretty pretty pretty please with sprinkles and a cherry on top
Good job, I'm so proud of you!
CIT{2G20kX09yF3F}
```
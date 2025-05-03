# Read Only - Writeup

| Author           | Title             | Category   | Difficulty |
|------------------|-------------------|------------|------------|
| barrythecanary | Read Only | reverse engineering | - |

## Description

Here we go!

Flag Format: CIT{example_flag}

## Attachment

[readonly](./readonly)

## Solution

I just ran strings on it and looked with grep for the flag start and well there it already was.

```
$ strings readonly | grep "CIT"
CIT{87z1BjG1968G}
```
#  Very Rotten - Writeup

| Author           | Title             | Category   | Difficulty |
|------------------|-------------------|------------|------------|
| barrythecanary | Very Rotten | crypto | - |

##  Description

`TFJDe0gzeV9ldmlfdzMzX0FYQ0M2V19Wa1hidldINDYxTXR1YlgyOXZnYn0=`

Flag Format: CIT{example_flag}

##  Solution

Looking at it the encrypted message I was pretty sure it's base64 encoded so I just decoded it on [base64decode](https://www.base64decode.org/) and got the following:

`LRC{H3y_evi_w33_AXCC6W_VkXbvWH461MtubX29vgb}`

Now it resembles a flag but had a different start at the front I assumed it was ROT encoded like the preceeding crypto challenge called "Rotten". I ran it on [dcode.fr](https://www.dcode.fr) and went through them till I found one that started with "CIT" and found the following for ROT9.

`CIT{Y4p_vmz_n44_ROTT7N_MbOsmNY572DklsO30mxs}`

This isn't quite the flag yet though. Based on how "CIT" is correct and there is also the "ROTT7N" part I assumed it must be partially decrypted. I also think the first leet word should be "You" or "Y0u". That would also be correct for "ROTT7N",  that should probably be "ROTT3N". I think based on if it's uppercase, lowercase or a number it's using a different rotation. I tried it again on dcode but used a custom alphabet (case sensitive) and only went with lowercase letters. My goal was to get the p from "Y4p" to become a u. that would take 5 rotations to the right. in the case of ROT I used -5. This worked pretty well and I got:

`CIT{Y4u_are_s44_ROTT7N_MgOxrNY572DpqxO30rcx}`

You can see the "are" after "Y4u" which I think is a good indicator it's correct. I tried ROT with only numbers this time and used ROT4 to get the final flag:

`CIT{Y0u_are_s00_ROTT3N_MgOxrNY138DpqxO96rcx}`

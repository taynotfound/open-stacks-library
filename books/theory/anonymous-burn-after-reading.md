---
title: "Burn After Reading: One-Time Pad Encryption Using Dice - Anonymous"
author: "Anonymous"
date: "2025/10/28"
category: "theory"
source: "https://theanarchistlibrary.org/library/anonymous-burn-after-reading"
source_name: "theanarchistlibrary.org"
page_type: book
mirror_state: full
description: "<center Vernam Cipher / One-time-pad </center ---------------------------- The Vernam Cipher or One-time-pad (OTP) is an encryption technique which does not always rely on computers and, if performed properly, is unbreakable. 1. Generating"
tags:
  - "theory"
  - "opsec"
  - "security culture"
  - "pdf"
files:
  - name: "Burn After Reading.pdf"
    type: "PDF"
    url: "https://raw.githubusercontent.com/taynotfound/open-stacks-library/main/files/tal-anonymous-burn-after-reading.pdf"
    hosted: true
  - name: "Burn After Reading.epub"
    type: "EPUB"
    url: "https://raw.githubusercontent.com/taynotfound/open-stacks-library/main/files/tal-anonymous-burn-after-reading.epub"
    hosted: true
---

# Burn After Reading: One-Time Pad Encryption Using Dice

*by Anonymous*

<center>
Vernam Cipher / One-time-pad
</center>

----------------------------

The Vernam Cipher or One-time-pad (OTP) is an encryption technique which does not always rely on computers and, if performed properly, is **unbreakable**.

**1. Generating the key:** generating the key (the one-time-pad) can be done in many ways, but one of the easiest ways which ensures (close to) true randomness is by rolling some **10-sided dice** (d10).

You can buy polyhedral dice at your local games/comic shop, or buy a bag of 50 d10s online.

Roll the dice as many times as it takes to obtain a key of the desired length. Write the key on a piece of graph paper. **Make only as many copies of the key as is needed to communicate.** Multiple keys can be generated in one session and put into a notepad.

**NOTE** on random number generators: There are many kinds of random number generators (**RNGs**). Generally, there are 2 categories. There are **True** random number generators (**TRNGs**) and there are **Pseudorandom** number generators (**PRNGs**).

**TRNGs** are **hardware** devices that rely on a **natural** source of randomness such as dice, a complete deck of properly shuffled cards, ambient noise, the avalanche breakdown of a diode, etc. There are even TRNGs that rely on the known rate of radioactive decay of certain materials.

**PRNGs** are usually software based. Examples of PRNGs include

Google's random number generator, dice roller programs, and the /dev/random file built into Linux systems.

**Randomness** is an interesting mathematical concept that's more complex than we can get into here. In all honesty, True randomness is actually very hard to obtain. In most cases the best you can hope for is "good enough". But while PRNGs may be "good enough" for most applications like playing tabletop RPGs with your friends, it's important to try to do Better than a program running on a computer or a network which may be compromised or whose code may be flawed.

**2. Encrypt your message:** Let's say you want to encrypt the message

"hello world" and your key is as follows:

85228 73961 05012 26896 59691 11361 30552 93412 49142 62259

We assign two-digit numerical values to each letter of the alphabet, with 01-26 being A-Z, and 00 being space.

| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 |
| _ | A | B | C | D | E | F | G | H |
| |
| 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
| I | J | K | L | M | N | O | P | Q |
| |
| 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
| R | S | T | U | V | W | X | Y | Z

(numbers 27-99 can be assigned other values such as lower-case letters, punctuation marks or whole common words **if you like**, but let's keep it simple for this example.) So the numerical value of the message "HELLO WORLD" becomes:

08 05 12 12 15 00 23 15 18 12 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00

To encrypt the message, we add the digits of each letter to the corresponding digits in the key, modulo 10 (%10). All this means is that if the number we end up with is greater than 10, we drop the first digit and only write down the second digit.

<verse>
H <verbatim>=</verbatim> 08
0 + 8 <verbatim>=</verbatim> 8
8 + 5 <verbatim>=</verbatim> 13
13 mod 10 <verbatim>=</verbatim> 3
encrypted "H" <verbatim>=</verbatim> 83
</verse>

Repeat the process for the next letter in the message:

<verse>
E <verbatim>=</verbatim> 05
0 + 2 <verbatim>=</verbatim> 2
5 + 2 <verbatim>=</verbatim> 7
encrypted "E" <verbatim>=</verbatim> 27

L <verbatim>=</verbatim> 12
1 + 8 <verbatim>=</verbatim> 9
2 + 7 <verbatim>=</verbatim> 9
encrypted "L" <verbatim>=</verbatim> 99

L <verbatim>=</verbatim> 12
1 + 3 <verbatim>=</verbatim> 4
2 + 9 <verbatim>=</verbatim> 11
11 mod 10 <verbatim>=</verbatim> 1
encrypted "L" <verbatim>=</verbatim> 41
</verse>

If we continue this process until the end of the message, we end up with

83 27 99 41 76 05 24 37 76 08 53 69 11 13 61 30 55 29 34 12 49 14 26 22 59

as our encrypted message.

**Key <verbatim>=</verbatim>** 85 22 87 39 61 05 01 22 68 96 59 69 11 13 61 30 55 29 34 12 49 14 26 22 59

**text <verbatim>=</verbatim>** 08 05 12 12 15 00 23 15 18 12 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00

**ciphertext <verbatim>=</verbatim>** 83 27 86 38 76 05 24 37 76 08 53 69 11 13 61 30 55 29 34 12 49 14 26 22 59

This is where you send the ciphertext to the recipient, and destroy the key so that it can't be used again.

**3. Decrypt the message:** In order to decrypt the message, we do the same process in reverse. So we subtract the key from the ciphertext digit by digit. If the difference is a negative number, we modulo 10 in the opposite direction and add 10 to get the correct number.

<verse>
ciphertext <verbatim>=</verbatim> 83
key <verbatim>=</verbatim> 85
8 - 8 <verbatim>=</verbatim> 0
3 - 5 <verbatim>=</verbatim> -2 (or if the number is smaller than what is subtracted from it, add 10) -2 +10 <verbatim>=</verbatim> 8
decrypted 08 <verbatim>=</verbatim> "H"

ciphertext <verbatim>=</verbatim> 27
key <verbatim>=</verbatim> 22
2 - 2 <verbatim>=</verbatim> 0
7 - 2 <verbatim>=</verbatim> 5
decrypted 05 <verbatim>=</verbatim> "E"

ciphertext <verbatim>=</verbatim> 99
key <verbatim>=</verbatim> 87
9 - 8 <verbatim>=</verbatim> 1
9 - 7 <verbatim>=</verbatim> 2
decrypted: 12 <verbatim>=</verbatim> "L"
</verse>

And continue the process until the end of the ciphertext. The result should be:

<verse>
decrypted <verbatim>=</verbatim> 08 05 12 12 15 00 23 15 18 12 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00
text <verbatim>=</verbatim> H E L L O    W O R L D
</verse>

**Tips:**

 1. **Keep messages** as **short** as possible. Since the messages will be encrypted and decrypted **by hand**, unnecessarily **long messages** will be very tedious to deal with.

 1. If the entire message is shorter than the length of the key, it is best practice to send the rest of the key as well. They will return zeros when decrypted, but will look like random numbers to anyone trying to crack the cipher. This is fine since you'll never use the same key again, and no information can be gleaned just from the length of the message.

 1. It's also a good idea to begin the message with an identifier such as "key n" or use the first 5 digits of the key itself (and start the message on the *next* set of digits) to let the recipient know which key from the one-time-pad they should be using.

**Conclusion:** Vernam Ciphers are a slow, tedious, low-bandwidth encryption tool that requires practice and discipline. But the tradeoff is unbreakable encryption. When American and Soviet spies used this type of communication during the Cold War, the encryption was cracked because spies were either lazy or low on resources. They tried to save paper by reusing keys. This allowed opponents to use frequency analysis on the intercepted messages, and eventually extract the keys which would allow them to decipher future messages.

Do not neglect the **ONE-TIME** aspect of the One-time Pad. Hence the title of this document, “Burn After Reading”.

There is no app for this, not really. If this is the type of communication you find to be necessary, it should be a foregone conclusion that you can’t trust your computing devices with the information you’re sending. As the saying goes, we’re all we’ve got.

<center>
/eof
</center>

[a-b-anonymous-burn-after-reading-2.png 20f]()

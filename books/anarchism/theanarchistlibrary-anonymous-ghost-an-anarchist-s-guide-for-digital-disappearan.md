---
title: "GHOST"
author: "Anonymous"
date: "2025"
category: "anarchism"
source: "https://theanarchistlibrary.org/library/anonymous-ghost-an-anarchist-s-guide-for-digital-disappearance"
source_name: "theanarchistlibrary.org"
page_type: book
mirror_state: none
language: "en"
description: "An Anarchist’s Guide for Digital Disappearance"
tags:
  - "english"
  - "anarchism"
files:
  - name: "anonymous-ghost-an-anarchist-s-guide-for-digital-disappearance.epub"
    type: "EPUB"
    url: "https://theanarchistlibrary.org/library/anonymous-ghost-an-anarchist-s-guide-for-digital-disappearance.epub"
    hosted: false
---

[Read on theanarchistlibrary.org](https://theanarchistlibrary.org/library/anonymous-ghost-an-anarchist-s-guide-for-digital-disappearance)

Some time ago, a friend of mine sent me a document called Digital Safety Tips for Organizers: Online Privacy Checklist to look over. I thought it was great and brought up a lot of important points regarding maintaining privacy if involved in activist activities. However, it inspired me to create more thorough documentation for individuals seeking to use technology as a tool for organization and direct action. With broader knowledge and application of digital self-defense, the tactics outlined here can be especially effective against the known capabilities of the current presidential administration and their goals. After all, who’s to say what strategies they will deploy to defeat “the opposition?” We’ve already seen some terrifying actions on this front, and, in my opinion, it’s best to be over-prepared.

Some of these suggestions may seem highly technical for the inexperienced individual, and therefore may present a bit of a learning curve. They may also seem like overkill or inconvenient. But I promise you, when it comes to the many ways an individual can be tracked and subsequently doxxed and/or investigated and arrested, it is worth it to take the time to learn and employ these tactics.

Depending on the actions taken, whether by an organization, collective, or otherwise anonymous individuals, one misstep can mean the end for you, and potentially your comrades, at the hands of law enforcement or some right-wing lunatic (if you can even tell the difference between the two). Please note that this is not an attempt at fear-mongering, but to prepare you and fortify your digital OpSec.

Because of the various skill levels among individuals, if any of these steps prove to be too difficult for you to safely employ, consider contacting a trusted and technologically-inclined comrade to assist you. If you are uncomfortable with the technicality of the outlined steps, it is probably best you do not approach anything like hacking, as you’re more likely to make missteps. But it is still important that you secure your online privacy. Approach the learning process with an open mind, and you’ll solidify a lot of useful knowledge that can be applied in various ways to maintain privacy and security in your online life, and will put you in a position where you can more easily keep up with changes in the digital landscape.

As always, assess your threat model and make decisions based on that. (Threat modeling is beyond the scope of this document but can be learned about through the No Trace Project). Additionally, this document will cover the tech aspects of operational security and won’t go very far into detail about correlation attacks and stylometry attacks (the former of which is when your usage of anonymous online activity is cross-referenced with your mobile device and other online activities, like using TailsOS to send out communiques and immediately shutting down your computer and going to the mall. The latter is analysis of your unique pattern of expression, like the way you usually communicate online [see: Who Wrote That? A zine by Zundlumpen #76]).

You can run your accounts through HaveIBeenPwned.com to see if your credentials have been included in any data leaks. Obviously, if they have, change your passwords immediately. It is best to use a secure password manager with a password generator built in so you can generate a strong password that you don’t have to remember.

There is a Linux command line tool called Breach-Parse that can be a bit more thorough when hunting for your own breached credentials. Instructions for installation and usage can be found at github.com/hmaverickadams/breach-parse

As you can imagine, having breached credentials floating around in database dumps is very dangerous, especially if you’re communicating with others about your activist activities.

Google yourself and take note of what you find about yourself through these searches. Is your address, phone number, email, etc, appearing in publicly available databases? Chances are if you’ve ever ordered anything online or signed up for a mailing list or put personal information literally anywhere on the internet, these things are out there for anyone to find either for free or for a very cheap price.

The Data Removal Workbook from IntelTechniques is a very useful tool toward the end of erasing yourself from the internet. However, you are likely in thousands and thousands of these websites. So it is faster and easier to use a service like Incogni or DeleteMe to achieve this. It costs money, and if you can afford to pay their monthly fee, it is absolutely worth it. If you find yourself unable to squeeze out the extra cash for these services, do NOT skip this step. Just do the work to remove your info from data broker sites.

• Delete your Facebook (and Instagram and Snapchat and Threads and on and on)

Are you using social media? Is it necessary that you use social media? Think of social media as a database of your personal information and behavior patterns. A determined adversary with a lot of resources can identify you just based on the way you casually communicate with others in the comments section or through your history of posts. You could also be publishing personally-identifying information without even realizing it.

It’s also important to consider that Meta has contracted with ICE to allow them pretty much unlimited surveillance on these apps. And you can bet they’re not limiting their watchful eye to undocumented immigrants. They’ve made it clear they’ll be flagging anyone that speaks ill of the U.S. Government. And you don’t want to give them the opportunity to stop you before you even get started, do you?

If you must use social media, I’d first recommend that you make use of the fediverse. SubMedia has an awesome platform called Kolektiva.social that has a Tor mirror. And the following advice is applicable to all platforms, especially if you have to use Facebook or Instagram:

Don’t use the same username across multiple platforms to avoid being tracked across several profiles. You don’t want to give an adversary a broader view of your activity.

Be mindful of what can be seen in photos you are posting. In 2016, 4chan users took note of circuit suspension towers in the background of a Syrian rebel propaganda video and were able to then use more of their videos to verify the landmark as well as satellite imagery to locate their base. They informed the Russian government through a journalist, who then carried out an airstrike on the base. Shia LeBeouf also fell victim to a harassment campaign from alt-right 4chan users employing the same physical OSINT tactics. So, know that this skill can be weaponized against you too.

Keep your personal profiles and activist profiles entirely separate. Any profiles you use to report on or talk about activist activities should be used with a pseudonym derived from something t hat is not personally connected to you. These profiles should only be accessed from behind a truly anonymous VPN and/or through the Tor network.

Do NOT access your activist social media accounts from your cell phone. You can use something like VirtualBox+BlissOS to isolate Android social media apps, which will all run behind a VPN if you’re running one on your host machine. If you must use a cell phone to access one of these profiles, get a burner smart phone and take out the SIM card and only ever use it on WiFi and with a logless, login-less VPN.

Or even twice. Use one unique password for every different thing you log into. This should go without saying but so many people still do this. Once one password is cracked, you’re fucked across the board.

The best recommendation is to use a password manager, and my recommendation of password managers is KeePassXC. It’s a local database, so it never touched the open internet. There’s a password generator feature that I use to create 30+ random character unique passwords for every separate account. And there are a plethora of additional security features to maintain the safety of your accounts, including two-factor authentication integration if you wish to use it.

Whatever you do, do not use the Google password manager through Gmail. If you Gmail password is cracked, it can be used to access all other passwords you have saved via the passwords subdomain. But you shouldn’t be using Google services anyway. The same rules apply to Google that apply to social media; it’s like a database of your internet activity.

Have you ever heard of a SIM swap attack? It’s when an attacker uses your publicly available information to trick your cell phone provider into sending them a SIM card for your phone number. It’s very common, very easy to pull off, and cell phone customer service agents don’t care if you’re actually the owner of the account; they just want to be sure your info can be verified. The entire purpose of this attack is to bypass your SMS-based 2FA. So, stop using that. Use an app that generates a time-based token like Authy (again, NEVER Google Authenticator).

Keep all of your email communications on encrypted email services such as Protonmail. Keep in mind, however, that Protonmail has been known to collaborate with law enforcement. There are a couple of ways to defend against the latter:

You can use PGP Encryption to ensure that your emails are only viewable by the intended recipients. Even if your account has been compromised, those that normally use your key to decrypt your messages will know an email that doesn’t use PGP was not written by you. This also pretty much eliminates the possibility of your affinity group/collective/etc from falling victim to a spear-phishing attack.

Email services like Thunderbird have built-in PGP features to make this easier.

For especially sensitive emails, especially if you can remain truly anonymous to the recipient (like sending communiques after an action), use a temporary, throwaway email address. A good service for this is tempr.email. This is especially powerful when coupled with TailsOS, which we will touch on a bit more later.

There are some great Tor services for email, as well. A couple examples would be RiseUp (which you need an invite link to use), Mail2Tor, and TorBox.

Use an encrypted messenger. Signal is a great option, especially since they introduced their username feature. Signal was created by anarchists for anarchists as well. It’s a favorite for communication among radicals.

Session uses an anonymous, decentralized network like Tor and can be used on PC only, unlike Signal. Session also uses a hash identifier instead of a username.

By far, the most secure encrypted messenger is Cwtch. Cwtch uses the Tor network to route messages, identifies you by hash only. It can be isolated to PC. And you can lock your profile behind a secure password.

Of course, it is up to your discretion who you communicate with through any of these channels. Be wary not to say anything to anyone that could link you to anything illegal unless you have built unshakable trust with the person on the other end. You can have the strongest encryption in the world, resistant even to quantum computers, and bad OpSec will render it completely useless.

Having said that, NEVER use Discord for any kind of organizing or discussion of protests or actions. Discord is known to be backdoored by several government agencies across the world. They actively collaborate with governments and law enforcement. Their voice calls are end-to-end encrypted, but I, personally, still do not trust that.

Stop using Windows. Now. Immediately. Using Windows and caring about privacy and security is like locking the front door because you’re afraid someone is going to come in through the back door. It makes no sense.

Windows telemetry is insanely invasive. Your entire operating system is tied to a Microsoft Account from which Microsoft collects data. There are Windows telemetry features that take automatic screenshots every few minutes and sends them back to Microsoft, which can be disabled manually. But fuck that.

Hackers, some of which are ultra-right-wing-Nazi-lunatics (see: Weev) and some of which are government actors (see: Sabu and the story of AntiSec), know that most of the world uses Windows, and therefore Windows is a low-hanging fruit whose security internals are widely known, and therefore develop malware specifically for Windows most of the time. And a lot of malware written for Windows these days will run without you even knowing with code that will make it undetectable to a virus scan while running as a process. If you think using an open-source EDR will save you, think again. EDR bypasses are common. Trust me. Hacks against Windows happen every single day, from everyday users to major corporations and government agencies that have the resources to pour millions into security.

Stop using Windows and overwrite your hard drive with a Linux distro. Or—better yet, buy a new SSD and install it and then install a Linux distro onto it. That way, Windows has never even touched your machine. My recommendation would be Pop_OS!, which is easy to use and focused on security. You can buy laptops and desktops with Pop_OS! preinstalled on them as well, the most secure option being System76, who build their PCs with specialized hardware meant for security.

If you’re ultra paranoid or doing high-risk activity online, use QubesOS, which basically runs almost every new window as its own isolated computer inside your computer. That way if you get compromised through one Qube, you can just close and wipe it and the rest of your system is safe. The setup is a bit more complicated and the hardware requirements are higher, but worth it if you need to use it. AnarSec has a great QubesOS guide that I would recommend.

Both of the operating systems I suggested force you to use full disk encryption. You will see it on the GUI installer. That way, if someone steals or confiscates your laptop, they can’t retrieve the contents of your hard drive.

For further information on this topic, I’d recommend Extreme Privacy: What It Takes to Disappear by Michael Bazzel.

This should be obvious, but there are still some things to go over:

You don’t want to use some VPN your favorite YouTuber is sponsored by, like ExpressVPN or anything you have to pay for with a credit card. Some of these claim they are logless, but your anonymity ends with your payment to them.

So, what you want to use is a logless VPN like RiseupVPN, which is free. But I highly recommend Mullvad VPN, which does cost money, but you can pay for it with Monero or buy a voucher so you can use it truly anonymously. Mullvad is also notorious for not working with law enforcement. So, install it, buy it safely, and turn that multihop feature on.

Either of these VPNs can be managed through command line or GUI application. Whatever you are more comfortable with at this point.

Your cell phone is a cop. It is probably best to never use it for anything sensitive ever. Which means it is a shame you can’t use the Signal app on your PC without having it installed on your cell phone. If you haven’t heard by now, Israel (surprise, surprise) sold malware to the Department of Homeland Security designed to hack your phone by sending a single message. It’s a zero-click installation. And once they’re in your phone, they can just open anything, including Signal, and spy on your activities.

The Trump administration has openly admitted that it will be surveilling and taking action against people that oppose ICE’s activities.

Buy a Google Pixel and de-Google it with GrapheneOS, which is basically QubesOS for cell phones. That way your Signal is kept separate from everything else, and it can’t be viewed by the alphabet boys when they send you that text. There are guides for this online for installing and using GrapheneOS, and I will again reference AnarSec. Even then, leave your phone at home for actions. Bring a burner (Tracfone ONLY) if you absolutely need a phone with you.

Turn biometric unlock OFF if you are going to be bringing your phone to situations where your chances of an encounter with cops is heightened (but seriously, please just don’t do this). Cops don’t need a warrant to point your phone at your face to unlock it and go through it.

Encrypt anything sensitive. Use VeraCrypt with a whirlpool algorithm, as this is the most secure. As with anything, make your decryption key something long and complex and definitely not words that appear in the dictionary—not even leet speech.

Sometimes encryption itself can be incriminating. And if you don’t give up the password to law enforcement if they want to look into your files for whatever reason, you can spend time in prison for obstruction. To bypass this, use hidden containers and hidden volumes.

Basically, you will have an outer container with some bullshit files you put in there that you’d plausibly make appear to need encryption, like a fake budget spreadsheet or something. This outer container opens with a separate password than your hidden container. Since encrypted data is just a jumbled mess, no one can prove there is a hidden container. You give this bullshit password for your bullshit files, and you have plausible deniability. Suck it, pigs.

You can also use VeraCrypt to encrypt your hard drive, which may be technically more secure than using the FDE on setup. But LUKS should be sufficient.

You can make your device tamper-evident with some stuff you probably already have lying around. This is important because if the cops do a covert search while you’re not home, they can easily install keyloggers or copy your storage or compromise your laptop in various ways if they have physical access to it. A keylogger will render your encrypted hard drive useless, since they’ll just record what you typed.

Take some small stickers and place them over the screws on the bottom of your laptop. Then take some clear nail polish and paint over the stickers. Before the nail polish drives, sprinkle some glitter. This way, you can tell if you’ve been victim to an Evil Maid Attack, and you’ll know you just need to not even turn on that laptop ever again.

Sure, if your device has been tampered with, you can just change your decryption key or something. But if they compromised the firmware—and they likely did—you ain’t getting rid of that virus ever. Just get a new laptop.

A MAC address is a unique identifier assigned to a network interface. This is different from your IP address, as an IP address changes based on which network you are connected to. A MAC address stays the same no matter what, and can therefore be tracked across networks.

Since you’re using Linux now, automatically spoofing your MAC address on bootup has never been easier. I’ll teach you how:

1. Open your command terminal and use the following command to find your network interface:

— Your network interface will be some weird name of random letters and numbers, and it’ll be associated with a local IP address: 192.168.xx.xx

2. Now that you know your network interface, you’re going to type this to open a text editor in your terminal:

**ALSO NOTE: install macchanger with this command: sudo apt install macchanger -y

4. and then you’ll use CTRL+S and CTRL+X to save and exit nano.

7. And then run this command once you save and exit and then you’ll be all done:

Now your MAC Address will be spoofed every time you turn on your computer.

Go into your settings and disable anything that sends info back to a service or company. This includes:

Use a timezone that is far away from where you live because of timestamps when sending data.

Disable Bluetooth. You don’t want shit being able to connect to your computer.

Set your trash to only keep files for one hour, and be sure to also set your temporary files to delete every hour.

Keep your username and hostname as generic as possible, for example: user@linux

Turn off automatic WiFi connection. While your MAC address may be spoofed, if you are being watched for some reason and your computer is searching for your home network, it will be linked to you.

Metadata is a big deal. If you take a photo with a smart phone, precise coordinates of where you were when you took the photo are attached to the photo’s metadata. Most services scrub this data on upload, however they usually store it themselves in their backend servers. So, it’s important to wipe metadata before posting photos or files or sending photos with a communique.

This is easily achieved with a tool called exiftool on Linux, like so:

Something else to consider is the fact that when you delete a file, it is not difficult to recover through the use of forensic tools. So, it is important to use tools that overwrite files a bunch of times to render them unrecoverable.

BleachBit is a good GUI application for this. And wipe is an easy-to-use command line interface tool that does 34 overwrites by default, but can do more if you use the flag to set a certain amount of overwrites.

Lastly, when you send photos, don’t just blur faces. There are AI tools that can unblur and depixelate photos. It is best to use the redaction tool in flameshot or greenshot (as seen in my command line screenshots in this document).

You should strive to use the Tor browser for everything if you can. I’d also recommend hiding from your ISP that you are using the Tor network. It’s not illegal to use Tor, but your ISP can still send agents to your house to ask you why you are using the Tor browser (which is insane, I know).

You can use a default bridge, send away for a bridge, or configure a bridge you already know to obfuscate your use of Tor. But you are also running a VPN, which will obfuscate your Tor usage as long as it is connected before Tor.

While using Tor, prioritize .onion sites, as they do not have exit nodes in the same way that clearnet sites do, many of which are owned by law enforcement.

Again, you do not have to be purchasing drugs from dark net markets or guns or doing anything remotely illegal to be flagged for using Tor and to become of interest to law enforcement. The chances are slim, but they are there. And since you’re doing activist stuff, you don’t want any extra attention from law enforcement, or your activities could be stifled.

If you are not going to be using Tor as your daily driver browser, that is totally fine. But I wouldn’t recommend any browser other than LibreWolf. Even Firefox betrayed us and is harvesting our data now.

As always use TailsOS when doing anything super sensitive. • Actually, I’m over here You can use a long-range wifi adapter to connected to public wifi networks miles away from your home from the comfort of your bedroom. If you’re skilled with hacking, some of these long-range wifi cards have packet injection capabilities, and you can use secure wifi networks after you grab and crack the hex for the WPA key.

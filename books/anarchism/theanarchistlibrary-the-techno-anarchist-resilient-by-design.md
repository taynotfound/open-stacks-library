---
title: "Resilient by Design"
author: "The Techno Anarchist"
date: "2026"
category: "anarchism"
source: "https://theanarchistlibrary.org/library/the-techno-anarchist-resilient-by-design"
source_name: "theanarchistlibrary.org"
page_type: book
mirror_state: none
language: "en"
description: "A Complete Guide to Decentralized, Private & Censorship-Resistant Technology From First Principles to Running Infrastructure"
tags:
  - "english"
  - "anarchism"
files:
  - name: "the-techno-anarchist-resilient-by-design.epub"
    type: "EPUB"
    url: "https://theanarchistlibrary.org/library/the-techno-anarchist-resilient-by-design.epub"
    hosted: false
---

[Read on theanarchistlibrary.org](https://theanarchistlibrary.org/library/the-techno-anarchist-resilient-by-design)

Install and configure systemd-resolved with DoH (Ubuntu/Debian)

Chapter 5: Virtualization — Running Many Computers Inside One

Step 2: Create the WireGuard configuration (Node A — 10.2.0.1)

Theory: BATMAN-adv — Better Approach To Mobile Adhoc Networking

Chapter 11: Content-Addressed Storage — Files That Cannot Be Deleted

Theory: Distributed Identity — Who Are You Without a Central Authority?

Application: Running Your Matrix Server as a Tor Onion Service

Alerting rules: critical alerts for resistance infrastructure

This book was written for two types of readers who share the same goal: building communication infrastructure that cannot be silenced.

If you are a complete beginner — you have never set up a server, you do not know what a VPN really is inside, and phrases like “DHT” or “P2P overlay” mean nothing to you — this book starts from first principles. Every concept is explained before it is used. Look for the blue Beginner’s Corner boxes; they are written specifically for you.

If you are intermediate — you know your way around Linux, you have maybe set up a home server — this book gives you the deeper theory and the real configuration examples to build production-grade distributed infrastructure. Look for the purple Going Deeper boxes for extra nuance.

How this book is organized: Each chapter follows the same structure. First, Theory — the why and how of the concept from first principles. Then, Application — the practical steps, configuration examples, and troubleshooting. You can read theory-only on a first pass, then return to application when you are ready to build.

All software described in this book is free, open-source, and used by journalists, researchers, human rights workers, and emergency responders worldwide. Knowledge of how technology works is not a crime anywhere in the world.

Understanding why this technology matters and what philosophy guides the entire guide

Understand the seven-step playbook that governments use to silence digital communications

Understand that each suppression technique has a technical counter-measure

When a government decides to suppress its population digitally, it does not flip one switch. It works through a predictable sequence of escalating measures, each targeting a different layer of the communications stack. Understanding this sequence tells you exactly which technologies you need — and in what order of priority.

Imagine postal workers who not only check the address on your envelope, but open it, read the letter, and decide whether to deliver it based on the content. DPI does the same thing with internet traffic — it inspects the content of data packets, not just their destination. This is how governments block VPNs (they recognize the “shape” of VPN traffic even if they cannot read the encrypted content). The counter-measure is to disguise VPN traffic so it looks like ordinary web browsing.

To understand what can be blocked, you must understand what authoritarian governments control:

Internet Service Providers (ISPs) — In most countries, ISPs must obtain a license. The government can revoke that license or issue legal orders to filter traffic. All internet traffic in a country passes through licensed ISPs.

DNS Resolvers — Most people’s computers use ISP-provided DNS resolvers. The ISP controls these and can make bbc.com resolve to nowhere, or to a government warning page.

Border Routers — Every country has a small number of connection points to the global internet (Internet Exchange Points). A government can order these to filter or block traffic.

App Stores and Hosting Providers — Apple and Google operate app stores in every country. A government can pressure them to remove apps. Similarly, hosting providers operating in a country can be ordered to take down content.

Physical Infrastructure — Fiber cables, cell towers, and exchange buildings are physical locations that can be raided, damaged, or controlled.

The key insight: Everything on this list is centralized. There are specific chokepoints — specific companies, specific buildings, specific people — that a government can pressure. The answer to all of it is decentralization — making the system have no chokepoints, no single company, no single building that controls it.

Complete internet shutdowns are rare and costly — they damage the economy, disrupt government services, and create international backlash. Most authoritarian regimes aim for selective suppression: block specific sites, monitor specific people, silence specific voices. That is what the tools in this book are primarily designed to counter.

Understand the core philosophy: eliminate every single point of failure and control

Pillar 1: Distribute. Never let any single machine, company, or location be essential to your communications. If the loss of any one component silences your network, that component is a liability. Build so that the loss of any component is automatically compensated for by the others.

Pillar 2: Encrypt. Assume all traffic is observed. Make the contents of that traffic meaningless to observers. End-to-end encryption means the only people who can read a message are the people it is addressed to — not the ISP, not the platform, not the government.

Pillar 3: Diversify. Do not depend on a single communication channel. If Matrix is blocked, use XMPP. If XMPP is blocked, use Tor. If the internet is down, use radio. Diversity means redundancy; redundancy means resilience.

Security and resilience professionals use a concept called “defense in depth” — multiple independent layers of protection, so that breaking through one layer does not compromise everything. Think of a medieval castle: a moat, then walls, then an inner keep, then a fortified room. An attacker must breach all layers to reach the treasure.

Layer 1: Physical — Hardware you own, encrypted disks, UPS power backup ↓ Layer 2: Network — Firewall, VPN, network segmentation (VLANs) ↓ Layer 3: Transport — TLS encryption on all connections ↓ Layer 4: Application — End-to-end encrypted messaging (Matrix/XMPP) ↓ Layer 5: Anonymity — Tor or I2P to hide who is talking to whom ↓ Layer 6: Content — IPFS/Hyphanet so content exists without a location ↓ Layer 7: Radio — HF/LoRa/APRS for when all internet is down You do not need all seven layers for every situation. Match your layers to your threat model (which Chapter 25 covers in depth). But understanding all seven tells you where your current gaps are.

Imagine your group needs to communicate secretly during a crackdown. You have a plan:

Normally: Use your private Matrix chat server, encrypted, over a VPN

If Matrix is blocked: Switch to your private XMPP server on a Tor onion address

If internet is throttled too badly: Use your local Wi-Fi mesh (BATMAN-adv) to communicate within the city

If everything is cut: Use handheld radios on prearranged frequencies with Morse code or digital modes

This book teaches you how to build all four of those fallback layers. By the end, losing any one — or even two — of them does not stop you.

Understand why Linux is the foundation for all the infrastructure in this book

Learn the key Linux concepts: processes, systemd, namespaces, cgroups, logging

Know how to install and navigate a Linux system for the first time

Linux is a free, open-source operating system kernel — the core software that manages your computer’s hardware and allows other software to run. Unlike Windows (owned by Microsoft) or macOS (owned by Apple), Linux is owned by nobody and everybody. Its source code is publicly available for anyone to read, audit, and modify.

This is not just a philosophical point — it has practical consequences for security and trust:

No hidden backdoors: Any backdoor in Linux’s source code would be visible to the millions of people who read and audit it. Proprietary operating systems make this kind of independent verification impossible.

No company to pressure: Microsoft has responded to government requests for data. Apple has removed apps at the request of authoritarian governments. The Linux Foundation has no products to sell in any country, no app store to police.

Complete control: On Linux, you decide exactly what software runs. Nothing installs itself, nothing phones home, nothing updates without your consent.

There are hundreds of Linux “distributions” (distros) — versions of Linux packaged with different software. For beginners, use Ubuntu Server 24.04 LTS or Debian 12 (Bookworm) . Both are stable, widely used, and have excellent documentation. “LTS” means “Long Term Support” — you will receive security updates for years without needing to upgrade.

User Applications (Matrix, IPFS, Docker, your scripts) ↕ System Libraries (libc, OpenSSL — shared code apps use) ↕ System Calls (the API between programs and the kernel) ↕ Linux Kernel (manages hardware, memory, processes, network) ↕ Hardware (CPU, RAM, disks, network cards) Theory: Processes — Every Running Program When a program runs on Linux, it becomes a “process” — an isolated instance of a running program with its own memory space. Every process has:

A parent process — most processes are started by another process

The key security principle: run every service as a non-root user with the minimum permissions it needs. If your Matrix server is compromised, it should only have access to the Matrix data directory — not to your WireGuard keys, your backup encryption keys, or your monitoring configuration.

When Linux boots, the first process that starts is systemd (PID 1). It is responsible for starting all other services in the correct order and keeping them running. Think of it as the city manager who makes sure all city services start up in the morning and restarts anything that crashes.

Every service on your system is described by a “unit file” — a configuration file that tells systemd how to start the service, what user to run it as, what to do if it crashes, and what other services it depends on.

Namespaces create isolated views of the system. A process inside a namespace sees only the resources in its namespace — its own network interfaces, its own process list, its own filesystem. From inside a container, it looks like you have your own computer.

cgroups (control groups) limit how much of each resource (CPU, memory, disk I/O, network) a process or group of processes can use. This prevents one misbehaving service from consuming all resources and crashing everything else.

pwd # Print Working Directory — where am I? ls -la # List files (l = detailed, a = include hidden files) cd /etc # Change to the /etc directory cd ~ # Go to your home directory cat /etc/hostname # Display the contents of a file less /var/log/syslog # View a file one page at a time (q to quit) Managing Services with systemd systemctl status matrix-synapse # Is the service running? systemctl start matrix-synapse # Start it systemctl stop matrix-synapse # Stop it systemctl restart matrix-synapse # Restart it systemctl enable matrix-synapse # Start it automatically on boot journalctl -u matrix-synapse -f # Watch the service's logs in real time # (-f means "follow" — keeps updating) Security Essentials # Update all software (do this regularly!) apt update && apt upgrade -y # Check who is logged in who # Check what ports are listening (what is exposed to the network) ss -tlnp # Check firewall rules nft list ruleset # View recent login attempts (look for brute-force attacks) journalctl _SYSTEMD_UNIT=sshd.service | grep "Failed password" | tail -20 Creating a Service Unit File (Example: a simple service) # /etc/systemd/system/myservice.service [Unit] Description=My Custom Service After=network.target # Start after networking is up Requires=postgresql.service # Start after PostgreSQL is ready [Service] Type=simple User=myserviceuser # Run as a non-root user WorkingDirectory=/opt/myservice ExecStart=/opt/myservice/bin/start Restart=on-failure # Restart if it crashes RestartSec=5 # Wait 5 seconds before restarting [Install] WantedBy=multi-user.target # Start in normal (multi-user) mode # After creating/editing: reload systemd, then enable and start systemctl daemon-reload systemctl enable --now myservice Going Deeper: Linux Security Modules

AppArmor (used on Ubuntu) and SELinux (used on RHEL/Fedora) are Mandatory Access Control systems. Where normal Linux permissions say “this user can read this file,” AppArmor adds “this specific program can only access these specific files and network ports, regardless of what user it runs as.” Even if an attacker exploits a vulnerability in your Matrix server, AppArmor can prevent them from reading files outside the Matrix data directory. Enable and configure AppArmor profiles for all sensitive services.

Linux is the only OS suitable for privacy-critical infrastructure because its code is fully auditable

Every service should run as a non-root user with minimal permissions

systemd manages services — use it to start services automatically and restart them on crash

Update software regularly; monitor logs for signs of intrusion

Understand the OSI model and why layering matters for building resistance networks

Know how IP addresses, DNS, and routing work — and how each can be attacked and defended

Understand VLANs, network segmentation, and why they matter for security

All networking is built in layers. Each layer provides services to the layer above it and relies on the layer below it. This is one of the most important concepts in all of computing — understanding it lets you identify exactly where a problem or a block is occurring and what the appropriate counter-measure is.

Think of sending a letter internationally. Layer 7 is the actual letter content. Layer 6 is the language it is written in. Layer 5 is the ongoing correspondence between you and the recipient. Layer 4 is the envelope. Layer 3 is the address on the envelope. Layer 2 is the postal truck carrying it within a city. Layer 1 is the road the truck drives on.

Why this matters for resistance: When a regime blocks access to a website (Layer 7), you can tunnel through that block at Layer 3 using a VPN. If they block VPNs at Layer 3, you can obfuscate your VPN traffic to look like normal Layer 7 HTTPS traffic. If they block all internet (Layer 3), you can communicate at Layer 1 with radio. Understanding the layers lets you always find a counter-move.

Every device on a network needs an address so that data can be routed to it. IP addresses are these addresses.

IPv4 addresses look like 192.168.1.5 — four numbers from 0 to 255, separated by dots. There are about 4.3 billion possible IPv4 addresses. This seemed like a lot in the 1970s but is now running out.

IPv6 addresses look like 2001:0db8:85a3:0000:0000:8a2e:0370:7334 — eight groups of four hexadecimal digits. There are 340 undecillion possible IPv6 addresses (that is 340 followed by 36 zeros). Every device on Earth could have billions of addresses.

Private vs. public addresses: Some IP address ranges are reserved for private networks (inside homes and offices). These include 10.0.0.0/8 , 172.16.0.0/12 , and 192.168.0.0/16 . They cannot be routed over the public internet — your router translates them to your single public IP address (this is called NAT — Network Address Translation).

When you see 192.168.1.0/24 , the /24 is a “prefix length” that tells you how many devices can be in this network. /24 means the first 24 bits are the “network” part and the remaining 8 bits are for device addresses — giving you 254 usable addresses (192.168.1.1 to 192.168.1.254). /16 gives you 65,534 addresses. /8 gives you 16,777,214 addresses.

When you type matrix.example.com , your computer does not know the IP address of that server. It asks a DNS (Domain Name System) resolver: “What is the IP address for matrix.example.com?” The resolver looks it up and returns the answer.

How DNS censorship works: The government orders ISPs to return wrong answers for certain domain names. Your computer asks “What is the IP of bbc.com?” and the ISP’s DNS resolver returns either the wrong address (redirecting you to a government page) or nothing at all (making the site unreachable).

DNS-over-HTTPS (DoH) — Send DNS queries over an encrypted HTTPS connection to a resolver outside the country (e.g., 1.1.1.1 or 9.9.9.9 ). The ISP cannot intercept and manipulate the query.

Run your own DNS resolver — Your network queries authoritative servers directly, bypassing ISP resolvers entirely.

Tor — All DNS resolution happens at the Tor exit node, bypassing local DNS completely.

When your computer sends data to a server in another country, that data passes through many “routers” — devices that look at the destination IP address and forward the packet toward its destination. Routers share information about which networks they can reach using routing protocols like BGP and OSPF.

BGP (Border Gateway Protocol) is used between organizations — between ISPs, between countries. It is how the global internet is “stitched together.” Each organization announces which IP ranges it owns, and other organizations learn those announcements and route traffic accordingly.

Internet shutdown mechanism: A government can order ISPs to withdraw their BGP announcements. Suddenly the rest of the world’s routers do not know how to reach IP addresses in that country. The country disappears from the internet. This is what happened in Egypt in 2011, Myanmar in 2021, and Sudan in 2023.

A VLAN (Virtual LAN) is a way of creating logically separate networks on the same physical switch infrastructure. A packet tagged with VLAN 10 cannot reach devices on VLAN 20 without explicitly crossing a router with rules permitting it.

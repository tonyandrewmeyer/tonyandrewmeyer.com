---
title: "A better WannaCry advisory for schools"
date: 2017-05-14T19:21:02+12:00
slug: "a-better-wannacry-advisory-for-schools"
categories:
  - "rant"
tags:
  - "advisory"
  - "education"
  - "email"
  - "ransomware"
  - "school"
  - "security"
  - "wannacry"
---
The Ministry of Education sent out a very poor advisory to schools about "WannaCry" today, based primarily (from what it seems) on the poor information coming from CERT-NZ. The advisory contains several factual errors, which the Ministry should not be spreading to schools.
I've written an improved advisory (I'll update it as required).
# (An improved version of an) Urgent message from the Ministry of Education
The weekend media reported on a virus called WannaCry (also WannaCrypt, WanaCrypt0r, WCrypt, and WCRY) that infected many computer systems around the world over the last few days, including very prominent organisations such as the NHS in the UK.
It appears that few infections have occured in New Zealand, but it is possible that your school may have been, or may be, at risk. We are writing to let you know what you should do, and what we are doing to protect schools.
## What is WannaCry?
WannaCry is a combination of a computer worm (software that spreads itself) and ransomware (software that encrypts files on a computer and demands a ransom payment to decrypt them). WannaCry spreads through a bug in Windows networking software, and once present in your network can quickly spread to all vulnerable devices.
The bug that is being exploited was patched by Microsoft two months ago (patch MS17-010), so systems that are running fully up-to-date software are not at risk from this attack vector. The code is designed to target unpatched Windows 7 and Windows Server 2008 (or earlier OS) systems, so Windows 10 systems are also not affected by this attack.
## How can you protect your school?
* Ensure that your software is up to date, and enable automatic updates wherever possible. If you are running an unsupported version of Windows (e.g. Windows XP), ensure that you install the special one-off patch that Microsoft have provided (link at the end of this notice), and upgrade to a supported version as soon as possible.
* If you have the technical capability to do so, disable SMBv1 with the steps provided by Microsoft: https://support.microsoft.com/kb/2696547
* If a user has an infected device, do not permit it to connect to your network.
* Ensure that you have a reliable backup system in place. A good rule of thumb is "3 2 1" - at least three copies, in two different formats, with one of the copies off-site - for every file that you would not want to unexpectedly lose.
* Upgrade your Windows computers to Windows 10.
* Although the spread of WannaCry was not via email, it is possible that some initial infections were, and email remains a significant vector for ransomware attacks. Ensure that your email goes through reliable filtering (anti-spam, anti-phishing, anti-malware) before it reaches your system. You should also remind your staff and students to always be careful opening attachments and links. Even when the sender is, or appears to be, someone trusted, the attachment/link may not be safe, as the sender's system may have been infected.
* Although not utilised by WannaCry, much ransomware is spread via malicious "macros" in Office documents (Word, Excel). Ensure that macros are disabled, and, if you have the technical capability to do so, that users cannot enable macros.
If your school has been infected, please report the incident to CERT immediately via its website: https://www.cert.govt.nz/businesses-and-individuals/report-an-issue/ and do not pay the ransom.
## What is being done about it
N4L has blocked all traffic on the Managed Network that is attempting to connect to malicious IP addresses known to be associated with this virus. They are also actively monitoring the Managed Network to spot traffic patterns that may indicate suspicious activity from connected devices.
## More information
- Easy to read summary: https://www.wired.com/2017/05/ransomware-meltdown-experts-warned/
- Microsoft customer guidance: https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
- Microsoft's advisory, including links for patches for unsupported versions of Windows: https://blogs.technet.microsoft.com/mmpc/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/
- How the initial attack was stopped: https://www.malwaretech.com/2017/05/how-to-accidentally-stop-a-global-cyber-attacks.html
- General information: https://krebsonsecurity.com/tag/wanna-cry-ransomware/
Unfortunately, the newly formed New Zealand Computer Emergency Response Team (CERT) has not managed to provide accurate or timely information about this attack. We recommend that you rely on other sources of information until this government agency is better equipped to deal with these types of situation.

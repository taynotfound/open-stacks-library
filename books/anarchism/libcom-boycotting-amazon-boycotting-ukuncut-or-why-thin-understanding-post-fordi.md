---
title: "Boycotting Amazon Boycotting Ukuncut Or Why Thin Understanding Post Fordist Capitalism"
author: "Main navigation"
date: ""
category: "anarchism"
source: "https://libcom.org/article/boycotting-amazon-boycotting-ukuncut-or-why-thin-understanding-post-fordist-capitalism"
source_name: "libcom.org"
page_type: book
mirror_state: none
language: "en"
description: "An excellent, friendly critique of UK Uncut&#039;s call to boycott Amazon, from By Strategy."
tags:
  - "en"
  - "anarchism"
  - "libcom"
files:
  []
---

[Read on libcom.org](https://libcom.org/article/boycotting-amazon-boycotting-ukuncut-or-why-thin-understanding-post-fordist-capitalism)

An excellent, friendly critique of UK Uncut's call to boycott Amazon, from By Strategy .

There are currently circulating calls for a boycott of Amazon this holiday season called by UKUncut and others . The stated reason here is that, as reported in the Guardian , Amazon have made 7 billion in sales, but pay no UK corporation tax. I’ll leave the specifics of the pledge aside, but let’s dive into what Amazon do as a corporation. It should be noted through all of this that Amazon are monopolist , union busting scumbags, with little regard for workers rights . I am far from cheerleading them as a company. This post is also intended to be a critical friend of UKUncut. But the fact is that UKUncut are using Amazon to host their website, all the while calling for a boycott of it . Unraveling this shows a lot about what is wrong about UKUncut and anti-tax avoidance campaigns broadly and where we must go now. It also shows how capitalism has changed and how we must adapt to oppose it.

Amazon have since aggressively been expanding its web services portfolio to huge success. Their cloud offering is now a core component of their business strategy. Perhaps most technically impressive offering is Amazon Elastic Cloud Compute (or EC2) - which is huge . In the past a server was a physical machine in an exact physical location. Now far more often the hardware is irrelevant and servers themselves are simply virtual machines, with no mapping of one machine to one server. EC2 takes advantage of server virtualisation technology and uses Amazon’s massive infrastructure to allow you to host virtual servers on their hardware. So in five minutes, one can spin up a Linux (or almost any OS) instance and start running a complex web application. The power of all this means many companies have decided not to buy traditional servers, but simply back their own work on Amazon’s technology. There is a category of more advanced “platform as service” platforms that abstract even further away from the physicality of servers, Heroku being the main example. If you are a “startup” looking to “ship” your new web application, then you are going to use something like this. To scale the site up you just turn up a slider. This hasn’t even considered all the services that basically package and resell Amazon Web Services to a consumer as backup.

As should be clear by now, Amazon Web Services are a huge part of the contemporary internet. This is made clear whenever there is a outage for AWS as there were a couple of times this year. In April they brought down Reedit and Quora and a bunch of other big name sites. In June they brought down Instagram, Pinterest and Netflix as well as Heroku, bringing down all the applications in turn hosted on that. But these outages don’t scratch the surface. They never even touched the most widely used elements of AWS: S3 and CloudFront. Boycotting these would mean boycott a huge quantity of the files that actually make the pages render (CSS, images and JS) hosted on Amazon’s technology. In effect then, what UKUncut are proposing is to boycott a huge chunk of the contemporary internet. What would this look like?

Well, lets try it. Though AWS IP addresses range about its fairly easy to obtain a list of IP ranges for some of their most popular platforms - EC2 and CloudFront . You have to work out the IP range for Amazon S3 - some sites just serve their assets straight out of S3 without CloudFront 1 . Here is the likely incomplete list from an hour or so of hacking about. So I basically made my firewall boycott (i.e. block outgoing connections to) all these IP addresses - I used IceFloor for Mac OS X’s black list feature to make this easier. Suffice to say, the internet was somewhat difficult to use. Browsing about was pretty tough - so I tried pinging a few sites 2 . You can simulate this more easily by using AdBlock Plus and adding rules that block Amazon stuff 3 .

So remember how Google also avoided tax ? Maybe we should use plucky upstart Duck Duck Go (who don’t avoid tax)? Well, DDG is hosted on Amazon EC2! Instagram is gone, of course Heroku was and a number of others - with images and page simply broken left right and centre - you never know where AWS have spidered into. I wonder if the UKUncut site itself was up? No it wasn’t - why? Because the UKUncut.org.uk site is hosted by Amazon EC2 . Or more specifically through an Amazon Web Services reseller called Transnexis, I didn’t dig into it much more. To make matters worse, the images on the UKUncut home page are hosted on DropBox. DropBox use Amazon S3 to host all their files . So not only would an Amazon boycott mean really boycotting all their AWS stuff, but an Amazon boycott would mean not using the UKUncut website itself 4 .

This isn’t a yah boo Louise Mensch style talking point from the right wing “oh-they-use-Starbucks-how-dare-they-oppose-capitalism”. I’ve sat on the floors of banks and pretended they are hospitals and I am a friendly critic of theirs - it cannot be doubted they put tax avoidance on the map and made considerable innovations in the manner and organisation of protest. However, this sort of thing reveals three things. First, the limits of boycotts as a tactic. Second, the limits of UKUncut’s analysis of austerity within capitalism and capitalism broadly. Third, its unfortunate very narrow focus upon tax avoidance.

Boycotts aren’t an effective tactic for a variety of reasons. First, modern supply chains, as this UKUncut example ably illustrates, are so dense it is impossible to avoid a particular company. Second, the idea of opposing consumerism by proposing ethical consumerism is problematic also. There is a huge literature on this. More often than not it moralises those who cannot afford to make these kinds of consumer choices (local bookshops, ethical eating, McDonalds versus local businesses etc) as bad, while failing to recognise, for example, stagnant wages. Finally, Amazon is neither going to be economically damaged nor morally persuaded by a boycott. Ask Nestle how effective long running boycotts are. Rather than all this battles must and should occur not at the point of exchange but at the point of production. UKUncut’s early shop invasion tactics, prior to the dispiriting defeat and resulting legal wranglings of March 2011, did real economic damage to companies first, by disrupting their trade and hitting at least marginally their profits directly. This tactic moves everything up a level, requiring alternative purchasing while pushing damaging and tiresome ethical consumerism. It is a retrograde step from their earlier moves.

Second, UKUncut’s analysis of capitalism and austerity has always been a bit paltry, given that it is a broad based group trying not to rock the boat too much in its media profile. An excellent episode of the Novara radio programme does a much better job of explaining this issue than I can. By not considering capitalism as a system it fails to understand why companies attempt to avoid tax. It is not simply because they are evil. It is because the system requires as much in order for companies to operate especially as markets become saturated and profits begin to fall. So Starbucks might throw a bit more tax in, but it needs to drive down its costs elsewhere, hence it begins discipling labour to cut costs . This is because in the UK Starbucks is simply not profitable . It must reduce its costs and will do this by any means - it is the way capitalism is .

Moreover, the fact that the government and Amazon and Starbucks are all in it together isn’t co-incidence , as another analysis notes, it a class acting as a class. At its best, UKUncut demonstrated this, as well as showing the cuts as clearly ideological, as clearly a choice - but a choice required by the logic of capitalism and growth. At its very best, UKUncut forced a NO to capitalist realism and suggested an outside . But it is neccessary to add to that this is a choice is because this choice is neccessary if capitalism is to continue as a mode of production. Again, Novara explains all this far better than I am. It is not simply some bad eggs. The UKUncut boycott call out clearly pits good (local, nice) against bad capitalism (evil multinationals) - yet the problem is capitalism itself 5 . Yet we cannot establish a position outside it, indeed, you must use its resources to fight against it. But this shouldn’t be feared - “here is a rose, dance here”! We all need to deepen our analysis of what capitalism is. We need to recall that the only solution to austerity is to move beyond capitalism as a means of organising time, work, production and ultimately our lives.

Third, and relatedly, we need to consider if focusing on tax avoidance is a good place to continue fighting. Maybe it is time to abandon it. UKUncut have prised open the discourse here, the mainstream can likely run with it, but Vince Cable and George Osbourne are not our friends. There is a partial victory, but no victory if the world we really want is not been gained. When companies didn’t avoid tax quite so much, capitalism was still a shit. There needs to be a re-think. We need something they can’t absorb so easily. Workers rights and workplace organising might be a good place to start (though outside the unions). Consider a nationwide day backing the formation of the Pret A Manger Staff Union throughout the country, with sit-ins and trying to get workers to join, with leaflets in multiple languages. A generalisation of this form of organising, but amplified by the internet. The best of what UKUncut did combined with the brilliant work others are doing .

But the analysis of what capitalism is must be part of this. An analysis that doesn’t think that capitalism hasn’t developed since the 1970s and we are still dealing with the Fordist factory worker. One that thinks about the changes in production that mean things like virtualised servers, Amazon Web Service, workfare and social-media-as-work are a reality. UKUncut couldn’t exist without this post-Fordist mode of production - it wouldn’t exist without Amazon Web Services. But this analysis shouldn’t conclude in a Louise Mensch style “gotcha”, but continue to examine what this means. It needs to talk about the medium - social media - through which it is realised in all its ambiguity - the fact social media is both a playground and a factory. We need to start understanding the system globally rather than firefighting contradictions only on terms appealing to our enemies.

just because you use a service doesn't mean you can't complain about it and encourage people to boycott it, in fact they are taking your money which you already paid your share of tax on and don't pay their fair share, so if you pay them money you have even more reason to protest and encourage others to boycott

your argument sounds like a pro amazon, conservative, right wing argument, things are not black and white, all or nothing, everyone can and should make a stand, whether they use amazon or not!

this guy is pretending to be against corporate tax dodgers, but in fact is telling anyone that uses any part of these tax dodging corporations that they have no right to complain and call a boycott, but in the real world if we buy a service we have more right to complain about it, because they take our money and in amazon's case avoid paying taxes!

Starbucks might throw a bit more tax in, but it needs to drive down its costs elsewhere, hence it begins discipling labour to cut costs. This is because in the UK Starbucks is simply not profitable. It must reduce its costs and will do this by any means - it is the way capitalism is.

I thought Starbucks UK basically paid all their profits back to a parent company in the Netherlands in the form of a sort of franchise fee, as a tax dodge - wasn't that the whole point of UKUncut targeting them?

Of course the whole issue is kind of academic. Even if Starbucks UK remains profitable, it still has to be profitable enough to be competitive and so on. And even if they could afford to just give money away, it's obviously in their interests to pass these costs on to their workforce rather than let it eat into whatever profits they're making.

Hey there swattoon - I didn't see your comment before I posted mine; anyway, a few thoughts.

just because you use a service doesn't mean you can't complain about it and encourage people to boycott it,

I don't think the author of the above piece is saying you can't complain about Amazon if you use their services. In fact they say:

This isn’t a yah boo Louise Mensch style talking point from the right wing “oh-they-use-Starbucks-how-dare-they-oppose-capitalism”.

What they're saying is that boycotting Amazon would be very difficult and probably not very effective. They also make some points about UKUncut's politics off the back of that.

your argument sounds like a pro amazon, conservative, right wing argument,

Have you read the above piece in full? I guess I find it hard to reconcile this impression of By Strategy's blog, with the actual written content of it. For example:

Amazon are monopolist, union busting scumbags, with little regard for workers rights. I am far from cheerleading them as a company.

Hardly a "pro amazon" position. I'm not sure where you see "conservative, right wing arguments" here either. The article criticises UKUncut for not going far enough in their anti-capitalism, and suggests focusing more on workplace organizing and workers rights. This is hardly a right wing position, is it?

this guy is pretending to be against corporate tax dodgers, but in fact is telling anyone that uses any part of these tax dodging corporations that they have no right to complain and call a boycott

Again, I don't know where you're getting this from, that isn't what this blog post says. It says that a boycott is a limited tactic because a) it would be very difficult for anyone to actually boycott Amazon altogether and b) boycotts aren't very effective at changing things anyway.

things are not black and white, all or nothing, everyone can and should make a stand, whether they use amazon or not!

I think you might want to take a look at your own post here before condemning others for "black and white" thinking. It seems like you've seen someone criticising UKUncut and have rushed to their defense without taking the time to read through and digest what that criticism was. Instead, I think you've projected views and opinions onto this article that aren't really there, or that actually contradict what the article is saying.

Starbucks might throw a bit more tax in, but it needs to drive down its costs elsewhere, hence it begins discipling labour to cut costs. This is because in the UK Starbucks is simply not profitable. It must reduce its costs and will do this by any means - it is the way capitalism is.

I thought Starbucks UK basically paid all their profits back to a parent company in the Netherlands in the form of a sort of franchise fee, as a tax dodge - wasn't that the whole point of UKUncut targeting them?

Of course the whole issue is kind of academic. Even if Starbucks UK remains profitable, it still has to be profitable enough to be competitive and so on. And even if they could afford to just give money away, it's obviously in their interests to pass these costs on to their workforce rather than let it eat into whatever profits they're making.

companies can do loads of things to make themselves appear not profitable when actually they are. Including paying things back to parent companies, setting up subsidiaries to sell wholesale to their own retail arms (like energy companies do in the UK), paying large executive salaries and into executive pension funds, etc. This doesn't mean that they aren't profitable.

But apart from this largely semantic point I wholeheartedly agree with the article above.

Even if Starbucks weren't dodging tax, they wouldn't be profitable. The FT sums it up nicely here: http://ftalphaville.ft.com/2012/12/11/1304382/losing-for-tax-purposes-a-diagram/

I think the statement on Starbucks not being profitable is coming from the Novara episode linked, give it a listen. Though in it they're talking about a wider crisis of profitability more so.

Hello - You have incorrectly listed TransNexus as the Amazon Web Services reseller who hosts UKUncut's website. TransNexus is actually a VoIP management software company. We do not host websites. I believe the hosting company you meant to link to is Transnexis Hosting.

Amazon 'used neo-Nazi guards to keep immigrant workforce under control' in Germany

http://www.nytimes.com/2015/08/16/technology/inside-amazon-wrestling-big-ideas-in-a-bruising-workplace.html

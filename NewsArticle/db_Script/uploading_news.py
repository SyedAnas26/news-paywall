def populate_news(apps, schema_editor):
    news_article = apps.get_model('NewsArticle', 'NewsArticle')
    news_article.objects.create(title='Trust in scientists on the rise worldwide', image='/news_image'
                                                                                         '/scientist_trust.jpg',
                                content="Trust in scientists has seldom been more crucial than now, with people "
                                        "having to make large-scale lifestyle changes based on guidance from experts "
                                        "during the COVID-19 pandemic.\n\n "
                                        "With scientists and those in the medical profession becoming increasingly "
                                        "visible in local and global media, this exposure appears to have had a "
                                        "positive effect.\n\nThe proportion of people expressing a high level of "
                                        "trust in scientists in their countries has increased in almost every region "
                                        "in the past two years, rising nine percentage points between 2018 and 2020 "
                                        "to 43 per cent globally.\n\nThis data is reported in the Wellcome Global "
                                        "Monitor for 2020, which delves into the impact of COVID-19 on livelihoods, "
                                        "and people’s views on science. It follows Wellcome’s 2018 Monitor, "
                                        "its first on public attitudes to science and health worldwide.\n\n East and "
                                        "South Asia, Australia and New Zealand, the Americas and Eastern Europe all "
                                        "saw rises of at least 10 percentage points between 2018 and 2020 in the "
                                        "proportion of people expressing a high level of trust in scientists in their "
                                        "countries.\n\nAnd globally the number of people professing a high level of "
                                        "trust in science itself rose to 41 per cent, from 31 per cent in 2018. "
                                        "\n\n“Trust is so important, both in science and in our health systems, "
                                        "and in governments, to ensure that public health can deliver,” says Beth "
                                        "Thompson, associate director of policy at Wellcome. “So, undoubtedly, "
                                        "it’s important that we develop that trust wherever we can around the "
                                        "world.”\n\nThe report findings also support the idea that growing trust is "
                                        "linked to scientists’ increased visibility in the media. “[It’s] "
                                        "particularly gone up among people who said they don’t know as much about "
                                        "science to start with,” says Thompson. “That could support the idea that "
                                        "it’s because people didn’t see a lot of science and didn’t have much access "
                                        "to it [before], and now, through the pandemic, they’ve had more exposure.”",
                                premium_content=False)

    news_article.objects.create(title='The Degradation of the Himalayas', image='/news_image'
                                                                                '/himalaya.jpg',
                                content="The Himalayan Mountains, going through the northern part of India separating "
                                        "it from the Tibetan Plateau, currently faces many issues. Either surrounding "
                                        "it’s public infrastructure, waste, and trash of all sorts, the Himalayas are "
                                        "in need of drastic change. \n\n Tourism rules this part of India’s economy, "
                                        "with the constant in and out nature of anyone seeking to climb the "
                                        "mountains. With increasing urbanization in the area, a problem of waste "
                                        "management makes it so garbage is spewed everywhere. Given it’s higher "
                                        "elevation, indefinitely colder climate, and poor public infrastructure, "
                                        "the Himalayas are riddled with trash. People are willing to pay and clean "
                                        "the Himalayas, but some lack knowledge on different disposal methods, "
                                        "and feel they do not have sufficient access to them.\n\nThis degradation of "
                                        "the environment and infrastructure causes air pollution, further destroys "
                                        "buildings, and ruins the economy of tourism in the region. The Himalayas "
                                        "utilize hydroelectric power, but need to further advantage of it to make it "
                                        "work entirely. The formation of dams not only displaced locals’ homes, "
                                        "but also greatly affected the environment for both land-going and aquatic "
                                        "animals. These dams, filled with pollution because of all the waste "
                                        "surrounding it, flow all the way into larger bodies of water all the way to "
                                        "the ocean. Due to climate change in the Himalayas, there is significantly "
                                        "less snow and ice, but more water is running down and being polluted.",
                                premium_content=False)

    news_article.objects.create(title='Climate Tyrants’ New Tactics', image='/news_image'
                                                                            '/climate.jpg',
                                content="Chief Justice John Marshall’s observation, “[t]hat the power to tax involves "
                                        "the power to destroy,” has become part of American political lore. Marshall "
                                        "understood that the state’s revenue-extracting power can be weaponized—even "
                                        "against those who have committed no crime. We are now seeing a corollary to "
                                        "that notion in finance, with fossil fuel companies as the target. It turns "
                                        "out the government may not need to tax your company into oblivion if it can "
                                        "isolate you from all sources of commercial financing.\n\nIt has become an "
                                        "article of faith among climate activists that it is not enough for ethical "
                                        "investors to voluntarily divest themselves from hydrocarbon holdings. "
                                        "Governments and central banks must intervene in capital markets to "
                                        "eventually drive such companies out of business. This strategy is not "
                                        "new—previous generations of activists sought to restrict capital to firms "
                                        "that produce military hardware, nuclear power, cigarettes, firearms, "
                                        "and other politically disfavored products. But never before has government "
                                        "policy so forcefully been part of the plan.In that spirit, the Senate "
                                        "Banking Committee held a hearing last year, titled “Protecting the Financial "
                                        "System from Risks Associated with Climate Change,” where members of the "
                                        "committee and witnesses were asked what the Federal Reserve was doing to "
                                        "save our planet from hydrocarbon-fueled climate disaster. One witness "
                                        "invited by the committee’s minority, however, had a different view. "
                                        "Economist John Cochrane of the Hoover Institution pushed back on the "
                                        "hearing’s premise that the federal government needs to be “protecting the "
                                        "financial system” from climate risks, suggesting that what climate policy "
                                        "advocates actually had in mind was to “steer funds to fashionable but "
                                        "unprofitable investments and away from unfashionable ones” via “regulatory "
                                        "subterfuge rather than above-board legislation or transparent environmental "
                                        "agency rule-making.”\nMany policies favored by climate activists are out of "
                                        "line with prudent policymaking. Worse, they may arrogate entirely new powers "
                                        "to the agencies involved. In his congressional testimony, Cochrane pointed "
                                        "out that the Network of Central Banks and Supervisors for Greening the "
                                        "Financial System—which the Federal Reserve recently joined—has a stated goal "
                                        "to “mobilize mainstream finance to support the transition toward a "
                                        "sustainable economy.” But that is not how finance regulation works. Agencies "
                                        "like the Fed don’t get to pick the policy goals that their leadership "
                                        "happens to like, pressuring private parties to immanentize those outcomes. "
                                        "The Fed has a specific statutory mandate regarding unemployment and "
                                        "inflation—it does not have plenary authority over the entire U.S. "
                                        "economy.\n\nFortunately, more people are recognizing that the Fed is about to "
                                        "get dangerously out of its depth on climate policy. For instance, "
                                        "in November, Joshua Kleinfeld of Northwestern Pritzker School of Law and "
                                        "Christina Parajon Skinner of Wharton wrote in National Review of the effort "
                                        "to transform the Federal Reserve into a climate regulator: “It is "
                                        "democratically illegitimate for the Fed to engage in freelance activism. The "
                                        "Fed has no legal right to do so.” In a 2021 Vanderbilt Law Review article, "
                                        "Skinner pointed out that the allegedly pressing nature of a societal problem "
                                        "doesn’t magically expand the legal powers of a given government entity. She "
                                        "explained, “despite the substantive importance of climate change, "
                                        "the U.S. Federal Reserve presently has relatively limited legal authority to "
                                        "address that problem head-on,” concluding that “many aspects of climate "
                                        "change sit outside the Fed’s legal remit today.”",
                                premium_content=False)
    news_article.objects.create(title='The Democracy Illusion', image='/news_image'
                                                                      '/illusion.jpg',
                                content="In America, “democracy” or “democratic” are among the most common words used "
                                        "to justify or endorse positions or policies. “Democratic” is attached as an "
                                        "adjective whenever something is considered good politically (e.g., "
                                        "“our democratic way of life”), and “undemocratic” is attached to things "
                                        "being criticized (including almost everything that represents a loss for "
                                        "just about anyone). \n\n Americans are constantly told we must fight for "
                                        "democracy. Leading up to elections, politicians extol the "
                                        "democratically-expressed wisdom of the electorate they hope to represent ("
                                        "that those elected often then ignore or overturn). We are told that the "
                                        "American Revolution was for democracy; that people have died for our "
                                        "democratic right to vote; that each vote was crucial; that if you don’t "
                                        "vote, you don’t care about America; and so on. We even hear proposals to "
                                        "replace the Electoral College because it isn’t democratic enough.\nSuch "
                                        "rhetoric ignores the fact that democracy can destroy liberty as well as "
                                        "preserve it. For a minor example, ask, “Would I have more or less liberty if "
                                        "a majority vote picked my clothes each morning and my dinner each night?” "
                                        "More importantly, ask, “Would I have more or less liberty if that was how my "
                                        "religion, my spouse, or my job was chosen, or how my take home pay was "
                                        "determined?”\n\nCurrently, the “democratic” equals “I approve” approach has "
                                        "turned into a cottage industry about how America and the world face massive "
                                        "threats to our democracy. Good examples are President Biden’s statement that "
                                        "“Democracy doesn’t happen by accident. We have to defend it, fight for it, "
                                        "strengthen it, renew it,” and his “Summit on Democracy” (ignoring the irony "
                                        "of how many things his administration has imposed or tried to impose against "
                                        "the wishes of most Americans). It is also illustrated by a Google search "
                                        "that turned up over 4.5 million hits for “threat to democracy.”\n\n",
                                premium_content=True)
    news_article.objects.create(title='Weekly Initial Claims for Unemployment Benefits Rise Slightly',
                                image='/news_image'
                                      '/employee.png',
                                content="Initial claims for regular state unemployment insurance increased by 23,"
                                        "000 for the week ending February 12, coming in at 248,000 (see first chart). "
                                        "That is the first increase following three weekly declines. Over the last 13 "
                                        "weeks, claims are up in seven weeks and down in six. The level over the last "
                                        "six weeks remains above the average in early January and February 2020 prior "
                                        "to the pandemic surge. However, by long-term historical comparison, "
                                        "initial claims remain very low.\n\nThe four-week average fell in the latest "
                                        "week – the second decrease in a row and the largest decline since December "
                                        "11, 2021 – coming in at 243,250, a drop of 10,500. Weekly initial claims "
                                        "data continue to suggest the labor market remains very tight.\n\nThe number of "
                                        "ongoing claims for state unemployment programs totaled 1.995 million for the "
                                        "week ending January 29, a drop of 35,244 from the prior week (see second "
                                        "chart). State continuing claims appear to be settling into a range just "
                                        "below their pre-pandemic level of 2.111 million (see second "
                                        "chart).\n\nContinuing claims in all federal programs totaled just 68,"
                                        "830 for the week ending January 29, a drop of 1,051. For January and "
                                        "February 2020, the average for Federal continuing claims was 34,174. Though "
                                        "the current numbers are above the pre-pandemic average, they are just a "
                                        "fraction of the 16.6 million peak and largely reflect the end of the "
                                        "emergency Pandemic Unemployment Assistance program and the Pandemic "
                                        "Emergency UC program.\n\nThe latest results for the combined Federal and state "
                                        "programs put the total number of people claiming benefits in all "
                                        "unemployment programs at 2.064 million for the week ended January 29, "
                                        "a drop of 36,295 from the prior week.\n\nDespite some volatility over the last "
                                        "few weeks, initial claims remain at an extremely low level by historical "
                                        "comparison. The recent wave of new Covid cases may have been a contributing "
                                        "factor to the volatility over the last few weeks. Still, the overall low "
                                        "level of claims combined with the high number of open jobs suggest the labor "
                                        "market remains very tight.\n\nContinuing labor shortages, along with materials "
                                        "shortages and logistical issues, are likely to continue to hamper the "
                                        "recovery in production across the economy, though declining new Covid cases "
                                        "should allow businesses to refocus on increasing output and ease some "
                                        "materials shortages and logistical bottlenecks. However, the overall "
                                        "shortage of labor may continue for some time and remain an obstacle to "
                                        "significant increases in output.",
                                premium_content=True)
    news_article.objects.create(title='Why China’s Aggression In Asia Is Backfiring', image='/news_image'
                                                                                            '/china.jpg',
                                content="As the dominant superpower since the end of World War II, the United States "
                                        "has played a core role in crafting the geopolitical status quo in Asia. US "
                                        "state-building operations were influential in the creation of liberal "
                                        "democratic regimes in Japan, South Korea, and Taiwan. Furthermore, "
                                        "the semblance of a rules-based international order is a hallmark of "
                                        "Washington’s work in the region, and it has inspired other nations to become "
                                        "stakeholders in upholding the same values. The CCP, with its newfound "
                                        "strength, understandably wishes to revise the current balance of power and "
                                        "alter the geopolitical equilibrium in Asia to better serve its interests. \n\n "
                                        "China’s increasingly aggressive behavior on the world stage might have "
                                        "scored some early victories, but it also alarmed its neighbors and the "
                                        "international community. A growing list of Asian countries seeks to contain "
                                        "Beijing’s ascendence to power within the region. As a result, the CCP will "
                                        "find it gradually more challenging to continue its path to challenge the "
                                        "United States for global hegemony. To paraphrase the great international "
                                        "relations realist, John Mearsheimer, the United States is blessed with "
                                        "friendly, weak neighbors to the north and south and fish to the east and "
                                        "west. The United States grew into a global superpower in part due to its "
                                        "geographic fortune, but China has no such luxury.\n\n China’s attempts to "
                                        "revise the power dynamic in Asia threaten American strategic interests and "
                                        "freedom-loving nations. With that said, the Chinese Communist Party (CCP) is "
                                        "learning the same foreign policy lesson as the United States. Countries "
                                        "don’t appreciate global powers belligerently pushing other nations around, "
                                        "or revisionist powers attempting to alter the geopolitical order. China’s "
                                        "authoritarian practices and territorial impositions earned few friends and "
                                        "many skeptics.\n\n Beijing’s situation is similar to Germany’s. It shares a "
                                        "continent with multiple peer competitors. As we are seeing in Asia, "
                                        "European history involved a constant balancing act of powerful states rising "
                                        "and competing against one another. Historian Melvyn Leffler pointed to this "
                                        "key fact, arguing that China’s rise to superpower status would be an uphill "
                                        "battle. \n\n China’s neighbors all present unique challenges. Even though "
                                        "Beijing occupies a seat of dominance on the continent, particularly in "
                                        "Northeast Asia, Japan does too. China’s northern neighbor and former global "
                                        "superpower, Russia, has a complicated relationship with Beijing. Let us not "
                                        "forget that the United States successfully pitted the Soviet Union and China "
                                        "against each other during the Cold War. To the south is India, "
                                        "another emerging global actor with the potential to be even more powerful "
                                        "than China. \n\n Alongside these formidable neighbors, the CCP has to contend "
                                        "with a growing list of smaller nations that still possess considerable "
                                        "leverage in their own right. These include South Korea, Australia, Taiwan, "
                                        "Singapore, and Vietnam. The Carnegie Endowment comments on the recent shift "
                                        "in Vietnamese attitudes towards China by noting, “As the Chinese government "
                                        "has grown more assertive and pushed the envelope in its dealings with "
                                        "Vietnam, Hanoi has performed a delicate balancing act with very little "
                                        "margin for error.” The balancing act includes warming ties with the United "
                                        "States across all spectrums; economic, cultural, and even military "
                                        "cooperation.\n\nBeijing’s maritime encroachments push countries like Malaysia "
                                        "and the Philippines towards the United States. Continued aggression will "
                                        "likely inspire more countries to seek closer ties with Washington. Although "
                                        "countries are apprehensive about getting involved in the United States’ "
                                        "rivalry with China, Beijing will experience growing resistance as its "
                                        "behavior becomes more disruptive to the current geopolitical status quo. ",
                                premium_content=True)
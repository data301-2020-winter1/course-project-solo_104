Analysis - Are Fancy Stats Useful in Predicting the Outcome of the Stanley Cup Playoffs?
---
---
First and foremost, a breif recap of the 2020 Stanley Cup Playoffs might be necessary to understand the analysis of the dataset.  
*Breifly* the playoffs occured simultaneously in "hub" cities of Edmonton, AB and Toronto, ON. The eastern conference playoffs took place in Scotiabank Arena in Toronto, while the western conference and finals occured in Rogers Center in Edmonton. To begin the playoffs a *play-in* round was necessary. The matchups for these were: PIT vs **MTL**, Tor vs **CBJ**, **NYI** vs FLA. and **CAR** vs NYR in the east and EDM vs **CHI**, NSH vs **ARI**, **CGY** vs WPG and **VAN** vs MIN. (bolded teams advanced). A visual of the resulting brakcet is provided in Images. 
The additonal rounds saw PHI, TB, BOS, and NYI advance in the east, VGK, VAN, COL, and DAL survived in the west. TB and NYI subsequently won their Conference Semi Final series, while VGK and DAL outlasted their opponents in 7 game thrillers in the west. 
DAL then defeated VGK rather easily to advance to the Stanley Cup for the first time since 1997, While TB defeated NYI to travel to Edmonton for the Finals. 
TB then defeated DAL in 6 games to claim their second Stanely Cup

*for team name descriptions, see* Legend 

---

To more accurately understand the process, we need to consider if TB had better underlying stats than any of the teams they beat en route to the Stanley Cup. Did the "Fancy Stats" say that TB deserved to win over each of CBJ, BOS, NYI and DAL? 

To conduct this analysis we need to construct comparisons of major "fancy stats" on a team-by-team basis: for effect, we will use PDO, CF%, SF, SA, SV%, SH%, xGF%, and HDSF%. With the exception of SA and Sv% these are measures of what extent the team was able to control a game with the theory that the team that controls the game wins most often. This is fairly intuitively correct - for most sports the better team will usually win - however hockey is known for championing *parity*, meaning the best team does not necessarily win. As Tyler Seguin said, "Analytics are [sometimes] overrated".   
  
1. First look at PDO. PDO is a combination of Save percentage and Shooting percentage. The expected value of PDO lies between 0.98 and 1.02, with values greater or less than these viewed as *lucky* and *unlucky* respectfully. From the list, we see that TB has average PDO of 1.014960. This indicates that they werent lucky and had SH% and SV% close to league averages. This measure shows that TB's Cup win wasn't *lucky*. Their opponents had the following respective PDO: CBJ (1.0105), BOS (0.906677), NYI (1.025455) and DAL (1.007308). In general BOS was *unlucky*, while NYI was *lucky*. DAL and CBJ both lost to a team with a very slighty better SH% and SV%. Consequentially, these two series were the closest on TB's cup run. The PDO values indicate TB deserved their Championship season. 
  
2. Second, observe CF%. CF% is a measure of how well a team managed to exert control on the game. Generally, good teams outplay their opponents and thus have a much larger share of CF%. It is worth noting that a teams construction and how their philosophical approach to a game can contribute a huge swing on CF%. For example, TOR had the 6th ranked CF%, which can be attributed to a play style of maintaining possession even if they have to regroup. TB had the 5th ranked CF% at 53.712, meaning they recorded about 54% of the shots taken for any given game. In general CF% greater than 50.000 is expected for winning teams (but this measure has many of the same problems all these stats face - they dont tell the whole story). While BOS scored fairly well in CF%, each of CBJ, NYI and DAL were bottom 8 teams. These teams got dominated offensively regularly throughout the playoffs. TB clearly controlled the game better than their opponents. 
  
3. Consider SV%, noting that high SV% shows that a goalie got *hot* and was able to carry a team for a short duration. In general higher SV% are indicitive of an unsustainable effort from the goaltender. TB ranked 9th with a 91.9 SV%. Each of NYI and CBJ ranked higher, while BOS had well below average goaltending. Further from part 1. It appears Boston was unlucky in the SV% area of PDO. This makes sense as starting Goalie Tukka Rask was unable to play due to a family emergency and BOS suffered consequentially. NYI and CBJ in particular seem to have been buoyed by tremendous goaltending. League average goaltending had SV% of 91.0%, meaning TB had SV% above league average. TB is known to have one of the best goalies in the league, which substantiates this claim. In short, TB's goaltending was very good, and contributed to their Stanley Cup Victory. 
  
4. Logically, looking at the other contributor to PDO should come next. SH% follow the same rules as SV%, as over time they will certainly regress to the average. DAL and NYI both shot very well, explaining their deeper postseason runs, although this indicates unsustainability. CBJ and BOS did not shoot as well, and therefore bowed out in the first and second rounds respectively. TB had middle of the pack SH%, meaning they were expected to keep scoring close to the rate at which they did. TB's SH% was sustainable. 

5. As far as xGF%, TB ranked a middling 10th league wide. A middle-of-the-pack ranking indicates that TB rarely lost by a large number of goals, and rarely won by a large number either. DAL and CBJ both ranked low on this metric, indicating that both teams won through defense more often than offense. These teams relied on a tight defense or above average goaltending to advance through the playoffs. BOS and NYI ranked simmilarly to TB, which indicates a good blend of Offense and Defense for these clubs. Note that all of BOS, NYI, CBJ and DAl are known as *defense first* teams. 
  
6. One of the stereotypical hockey sayings is "Pucks on Net". Hence, next consider SF%, a measure describing which team controls the overall shots in a game. TB ranks very well once again, controlling 54% of Shots in the average game. CBJ was particularly bad at this, while BOS, NYI, and DAL all ranked middle of the pack. This measure backs up the CF% measure discussed earlier, indicating TB was the dominant team throughout the playoffs. 

7. Since defense wins championships, consider SA. This measure will indicate teams that defend well, usually accomplished by controlling the play of the game. NYI, BOS, and TB all ranked well in this metric, indicating they provided excellent defense throughout the playoffs. CBJ ranks last, allowing almost 40 shots against per game. This shows that CBJ leaned heavily on superb, and likely unsustainable, goaltending. 

8. Lastly, Consider HDSF%. Teams that routinely get to the center of the ice offensively and can generate chances from the "homeplate" are usually set up for sucess. Moreover, preventing these chances are necessary to find any success in the playoffs. TB ranked very well once again, especially if you remove teams that failed to advance past the play in round (EDM, TOR, PIT). NYI also did well, while BOS and DAL were not as effective at limiting these chances. As previously stated NYI is proven to have played very efficient defense throughout the playoffs. It has become clear that TB also provided expectional defense on their quest for Playoff Glory. 

---
From each of the above 8 points, we see that TB had usually great underlying numbers, which indicate that TB certianly deserved their second Stanley Cup victory this summer. The discussed *fancy stats* indicate that TB was not lucky, nor did they play at an unsustainable level or run into a red hot goalie. Many of the measures indiacte that TB was the best Eastern Conference team, and were far superior to the Western Conference representative DAL. From the results of this analysis, it is clear that the *fancy stats* employed by NaturalStatTrick, as well as other statisticians, indicate that TB deserved to win. As TB did come away with the Stanley Cup, these metrics appear to have a clear ability to predict which teams are more likely to win. 

---

However: A possible problem appears in the Western Conference Semi Finals. Consider the same series of measures for VGK and DAL. Did DAL deserve to win from an analytical perspective? 

1. VGK had a slightly lower PDO than DAL, and both values lay in the accpeted region for the measure. Neither team benefitted from unsustainable SH% or SV% by the values emitted by the PDO measure. PDO does not indidcate that one team should have won over the other, nor that either team was lucky to acchive what they did. With just this one measure taken into account, it appears this series outcome was a coin flip. 
  
2. VGK were the best CF% team in the league by nearly two whole percentage points. DAL meanwhile left something to be desired, often getting out shot and subsequently losing the CF% measure. By this metric, DAL was the less dominant team, and VGK was more deserving of a series victory. 
  
3. DAL and VGK ranked 11th and 12th in SV% throughout the playoffs, meaning there was little difference between these factors for the teams. Note however that VGK had a lower PDO - if their SV% component was the same, then the SH% for the teams had to be different, and VGK must have fared worse. 
  
4. Indeed, Vegas managed a much lower SH%, at about 8% compared to DAL's 10%. Thus it appears that the key difference between the two teams is DAL managed to score more often. It is also worth noting that VGK SH% may have been hugely affected by the performance of VAN goalie Thatcher Demko, who limited VGK to just a 2.5 Shooting percentage through games 5, 6, and 7 at the end of the VAN vs VGK series. This outlier may have a huge effect on the overall SH% for VGK
  
5. VGK also ranked first in xGF%, while DAL was a bottom half team at this metric. This indicates that when VGK won, they did so by a larger margin than DAL. VGK had weak first and second round competition in CHI and VAN, which contributes to this number being as high as it is. 

6. VGK once again ranked first in the league in SF%, indicating an immense ability to control a game. DAL was near the bottom of the league in this metric as well, which clearly indicates that VGK significantly outshot DAL througout this series.   

7. Benefitting from weaker competition in general, VGK finished first in SA. Limiting the opponents ability to build any momnetum in the defensive zone is key to series vicotries and VGK proved to be exceptional at doing so. DAL ranked low, usually allowing a large volume of shots on their net. 

8. The trend continued with HDSF%, with VGK among the best teams in the league while DAL struggled. VGK proved to be a great defensive team in limiting high danger chances from its opponents while managing to generate its own consistently. DAL meanwhile usually allowed more high danger chances than they generated. 

---
So in contrast to the Eastern Conference, the Western Conference Finals did not do what the *fancy stats* suggested would occur. VGK appeared to be the far better statistical team. Why would this happen? VGK head coach Peter DeBoer was quick to suggest that VAN's Demko managed to destroy the confidence VGK had with shooting the puck, which caused VGK to be a little too pass-happy. DAL meanwhile appeared to have been extremely opportunistic with their offense, and managed to grab more *garbage goals*. Furthermore, this was a 5 game series. It is unlikely had the series gone to 7 games that DAL would have been able to withstand the VGK team. In short, DAL got lucky analytically. 

---

This brings up a conundrum in hockey: which method (eye-test or analytics) is better? The answer appears to be a blend, while parity limits how much one team can really be better than another. Using analytics to idetify weaknesses and to dictate where teams should try to expose another team can certainly be beneficial, but in general the better team wins - and usually the eye-test and analytics agree which team is better. It is clear that TB was the best team in the east and was certianly better than DAL, but analytics are a long way away from telling the whole story, as evidenced by the outcome of the DAL vs VGK Western Conference Final. Analytically VGK deserved the chnace to play on the Stanely Cup final,  
Are analytics overrated? Sometimes.  

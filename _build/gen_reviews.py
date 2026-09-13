#!/usr/bin/env python3
"""Writes _build/pages/3xx-review-*.html and the reviews hub.

The prose in COPY below is written per operator — the verdict, the cashier
account, the weaknesses, the FAQ answers. Only the scaffolding is generated:
front matter, the specification grid, the computed scorecard and clearance
table, and the internal links. That way every review carries the same
structure without every review carrying the same sentences.

Run this, then run build.py.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_build", "pages")
OPS = json.load(open(os.path.join(ROOT, "_build", "operators.json")))

COPY = {
 "smash": dict(
  n=300, rank=1, rate="45%",
  eyebrow="Ranked 1st of 11 &middot; 9 payouts timed",
  lede="Smash wins this site's ranking on one unusual fact: its welcome offer asks "
       "<strong>10x</strong> where almost everything else in this market asks 30x to 40x. That single term "
       "is the difference between a bonus that is a promotion and a bonus that is a decoration &mdash; and it "
       "is why Smash is one of only two offers here that models as worth more than it costs to clear. "
       "Nine timed withdrawals came back at a median of seven hours forty, none refused.",
  verdict="The best combination on this site of a bonus you can actually clear and a cashier that pays. "
          "If you are opening one account, open this one.",
  body="""
<h2 id="bonus">The bonus, which is the entire argument</h2>
<p>Smash advertises <strong>{{op:smash:welcome}}</strong> with wagering of <strong>10x on deposit plus
bonus</strong>. The base matters &mdash; deposit plus bonus is a larger turnover base than bonus alone &mdash;
but at a multiple of ten it is still a fraction of what the field charges. A 35x offer on the bonus alone
requires more than three times the turnover of this one.</p>
<p>Priced on a &pound;100 first deposit: a {{clear:smash:bonus}} bonus, {{clear:smash:turnover}} of required
turnover, an expected cost at 96% RTP of {{clear:smash:cost}}, and an expected net of
<strong>{{clear:smash:net}}</strong>. Every 35x offer on this site comes out negative on the same model. That
comparison is the reason Smash is first, and you can check the arithmetic yourself against the
<a href="/online-casinos/bonuses/">full clearance table</a>.</p>
<p>The surrounding terms are clean rather than clever. Maximum bet while wagering is &pound;5, which is
standard. Live games count 10%, which is also standard and means the bonus is a slots product. There is no
maximum-conversion cap buried in the promotion, which there very often is.</p>

<div class="callout tip">
<span class="t">Who this offer suits</span>
<p>Anyone who plays slots and intends to clear a bonus rather than decline one. At 10x, clearing is a
realistic project rather than a theoretical one &mdash; which is not something I can say about most of the
offers on this website.</p>
</div>

<h2 id="cashier">The cashier</h2>
<p>Nine withdrawals, a median of <strong>{{op:smash:ledgerMedian}}</strong>, a worst case of
{{op:smash:ledgerWorst}}, and nothing that needed chasing. The worst case was the first request, which is
where verification lands; from the second request onwards the spread was tight, which is the pattern you want
and does not always appear.</p>
<p>Balances are held in pounds, so there is no conversion spread in either direction &mdash; worth roughly
&pound;30 on a &pound;500 deposit and &pound;700 withdrawal against a euro-denominated site, and therefore
worth more than most bonuses. GBP methods run to {{op:smash:gbpMethods}}. The weekly cap is
{{op:smash:withdrawCap}}, which is high enough not to matter to most people.</p>

<h2 id="games">The games</h2>
<p>{{op:smash:games}}, with {{op:smash:providers}} among the studios. That is a middling catalogue by the
standards of this list &mdash; Kingdom carries more &mdash; but game count is the least meaningful number in
casino comparison, because every site resells the same studios. What matters is that the major feeds are
real, and they are.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>The licence is Anjouan</strong>, which is the lightest-touch regime of those represented on this
site. Complaints escalation is correspondingly weaker than under a Malta or reformed Cura&ccedil;ao licence.</li>
<li><strong>Support is adequate rather than good.</strong> Answers came within a few minutes at peak and
noticeably slower late at night, and the first response is scripted.</li>
<li><strong>The live floor is thin</strong> next to Seven's. If live dealer is your main game, this is not
the site for you.</li>
<li><strong>The interface is plain.</strong> Fine on a phone, unremarkable on a desktop.</li>
</ul>
""",
  faq=[
   ("Is Smash Casino legit?",
    "It operates under an Anjouan Gaming Authority licence and paid all nine withdrawals I requested, at a "
    "median of 7h 40m with no request refused or unexplained. It does not hold a UK Gambling Commission "
    "licence, so it sits outside GamStop and outside UK player protections — the Commission cannot act for "
    "you in a dispute. On the evidence I have, the cashier works."),
   ("What is the Smash Casino welcome bonus?",
    "600% in total up to £10,000 across the first deposits, with wagering of 10x on deposit plus bonus. The "
    "10x multiple is the important number: on a £100 first deposit that is a far smaller turnover "
    "requirement than the 35x offers elsewhere on this site, and it is why this offer models as net "
    "positive when most do not."),
   ("How long does Smash Casino take to pay out?",
    "A median of 7h 40m across nine requests I timed, with a worst case of 31 hours on the first withdrawal, "
    "which is when identity verification happens. Crypto is the fast route; card withdrawals take one to "
    "three working days, which is the card networks rather than the casino. Verify your account on day one "
    "and the first request stops being the slow one."),
   ("Does Smash Casino accept GBP?",
    "Yes, balances are held in pounds, which avoids the 2–4% conversion spread charged in each direction by "
    "sites that convert to euros. On a £500 deposit and a £700 withdrawal that spread is around £30 — more "
    "than most welcome bonuses are worth after wagering."),
   ("Is Smash Casino on GamStop?",
    "No. GamStop participation is a condition of holding a UK Gambling Commission licence, and Smash is "
    "licensed in Anjouan instead. If you are registered with GamStop, please do not use it — see our "
    "<a href=\"/responsible-gambling/\">responsible gambling page</a> for blocking tools that work "
    "regardless of where an operator is licensed."),
  ]),

 "kingdom": dict(
  n=310, rank=2, rate="45%",
  eyebrow="Ranked 2nd of 11 &middot; fastest cashier in the ledger",
  lede="Kingdom has the fastest cashier I have logged anywhere on this site. Eleven withdrawals, a median of "
       "<strong>three hours five minutes</strong>, and a worst case of nine hours &mdash; including one request "
       "made at twenty to three on a Sunday morning that landed before breakfast. It also carries the largest "
       "game library here. What keeps it second rather than first is the bonus: 30x is better than the field "
       "and still not good enough to price positive.",
  verdict="The site to choose if getting paid quickly is what you care about, and the one I would pick for "
          "game range. Decline the welcome offer and it is arguably the best account on this page.",
  body="""
<h2 id="cashier">The cashier, which is why it is here</h2>
<p>Eleven timed withdrawals at a median of <strong>{{op:kingdom:ledgerMedian}}</strong>, worst case
{{op:kingdom:ledgerWorst}}. That is the tightest distribution in my ledger &mdash; not merely the fastest
median but the smallest gap between typical and worst, which is the more useful property. A site with a
two-hour median and a six-day tail has a process that sometimes fails. This one does not.</p>
<p>Identity verification came back in {{op:kingdom:kycHours}}, which is fast for this market and is the
single biggest determinant of how your first withdrawal feels. Balances are in pounds.
{{op:kingdom:gbpMethods}} are available, and the cap is {{op:kingdom:withdrawCap}} &mdash; monthly rather
than weekly, and high enough to be irrelevant to almost everyone.</p>

<h2 id="bonus">The bonus</h2>
<p><strong>{{op:kingdom:welcome}}</strong> at <strong>30x on the bonus</strong>. Thirty is better than the 35x
and 40x that dominate this market, and the base is bonus-only rather than deposit plus bonus, which helps
again. It is still not enough.</p>
<p>On a &pound;100 deposit: {{clear:kingdom:bonus}} of bonus, {{clear:kingdom:turnover}} of turnover, an
expected cost of {{clear:kingdom:cost}} and a net of <strong>{{clear:kingdom:net}}</strong>. The honest
recommendation is to decline it at the cashier and deposit clean &mdash; at which point you have the fastest
cashier on this site with no wagering condition attached to your balance, which is a good place to be.</p>

<h2 id="games">The games</h2>
<p>{{op:kingdom:games}}, the largest library on this site, with {{op:kingdom:providers}} among the studios.
Nolimit City and Hacksaw are both present as real feeds rather than as logos, which matters if you play
high-volatility slots, and the Evolution live floor is genuine if not as deep as Seven's five-studio
arrangement.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>The licence is legacy Cura&ccedil;ao eGaming</strong>, the older sub-licence model now being wound
down in favour of direct Gaming Control Board licensing. Check whether it has migrated before you rely on the
complaints route.</li>
<li><strong>The bonus is better than the field and still negative</strong> once priced. Decline it.</li>
<li><strong>It is not a sportsbook.</strong> There is a betting section; it is not the reason to be here.</li>
</ul>
""",
  faq=[
   ("Is Kingdom Casino legit?",
    "It paid all eleven withdrawals I requested, at a median of 3h 05m with a worst case of nine hours — the "
    "fastest and most consistent record in my ledger. It holds a Curaçao eGaming licence rather than a UK "
    "one, so it is outside GamStop and outside UKGC protections, and the Gambling Commission cannot act for "
    "you in a dispute."),
   ("How fast does Kingdom Casino pay?",
    "Faster than anything else I have tested: a 3h 05m median across eleven requests, with nothing slower "
    "than nine hours including a request made at 02:40 on a Sunday. That is crypto; card withdrawals take "
    "one to three working days at Kingdom as everywhere else, because the card networks set that pace rather "
    "than the casino."),
   ("What is the Kingdom Casino welcome bonus?",
    "600% in total up to £9,500 across four deposits, at 30x wagering on the bonus. Thirty times is better "
    "than the 35x and 40x that dominate this market, but priced against a 96% RTP assumption the offer still "
    "costs more to clear than it gives. Declining it leaves you with the fastest cashier here and a balance "
    "you can withdraw at any moment."),
   ("Does Kingdom Casino have a withdrawal limit?",
    "£15,000 a month, which is high enough that most players will never meet it, and it is a monthly rather "
    "than weekly cap. Minimum withdrawal is £20. Always check the current cap at the cashier before "
    "depositing — a low cap is how a large win becomes an instalment plan, and terms change without notice."),
   ("Is Kingdom Casino on GamStop?",
    "No. It is licensed in Curaçao rather than by the UK Gambling Commission, and GamStop only covers UK "
    "licensees. If you are self-excluded, please do not register — device-level blockers such as Gamban work "
    "on sites like this one, and the National Gambling Helpline is free on 0808 8020 133."),
  ]),

 "rivo": dict(
  n=320, rank=3, rate="45%",
  eyebrow="Ranked 3rd of 11 &middot; biggest match, lowest wagering",
  lede="Rivo pairs the largest advertised match on this website &mdash; 1000% across the package &mdash; with "
       "<strong>10x wagering on the bonus</strong>, which is a combination almost nobody offers. Normally a big "
       "headline arrives attached to a requirement designed not to be met. Here it does not, and that is why "
       "Rivo is the second of only two offers on this site that model positive.",
  verdict="The best offer here for someone who actually wants to take a bonus, and a solid combined casino "
          "and sportsbook account. The cashier is a step behind the top two.",
  body="""
<h2 id="bonus">The bonus</h2>
<p><strong>{{op:rivo:welcome}}</strong> with wagering of <strong>10x on the bonus</strong>. Ten times, applied
to the bonus alone rather than to deposit plus bonus, is the cheapest structure on this site by turnover
required per pound of bonus.</p>
<p>Priced on a &pound;100 deposit: {{clear:rivo:bonus}} of bonus, {{clear:rivo:turnover}} of turnover, an
expected cost of {{clear:rivo:cost}}, and a net of <strong>{{clear:rivo:net}}</strong>. Alongside Smash, this
is one of two positive rows in the <a href="/online-casinos/bonuses/">clearance table</a>.</p>
<p>Two caveats worth reading before you accept it. The 1000% is a <em>package</em> figure spread across
several deposits, not a first-deposit match &mdash; the modelled figures above are for the first deposit only,
which is the one most people actually make. And the sports side of the welcome is a separate, much smaller
offer at 100% up to &pound;500.</p>

<h2 id="cashier">The cashier</h2>
<p>Eight withdrawals, median <strong>{{op:rivo:ledgerMedian}}</strong>, worst case
{{op:rivo:ledgerWorst}}. That is a clear step behind Kingdom and Smash &mdash; eleven hours rather than
three, and a three-day tail rather than a nine-hour one. Nothing was refused and nothing needed chasing, but
the distribution is wider, and a wider distribution is what a less mature payments operation looks like.</p>
<p>Balances are in pounds. {{op:rivo:gbpMethods}} are supported, minimum withdrawal
{{op:rivo:minWithdraw}}, cap {{op:rivo:withdrawCap}}. Verification took {{op:rivo:kycHours}}, which is
slower than the top two and is most of why the first request was the slow one.</p>

<h2 id="sportsbook">The sportsbook</h2>
<p>Rivo is the best of the combined casino-and-betting accounts here, which is a real convenience: one
balance, one verification, one withdrawal queue. Football coverage is deep and Asian handicap markets are
priced keenly. Racing is thin, as it is at every offshore book &mdash; see
<a href="/online-betting/">online betting UK</a> for why that is structural rather than an oversight.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>The cashier is mid-table.</strong> Eleven hours is fine; three hours is better, and Kingdom does
three.</li>
<li><strong>The 1000% headline is a package figure</strong>, not a first-deposit match. Read the tranche
terms before planning around it.</li>
<li><strong>{{op:rivo:games}} is the smallest catalogue in the top five.</strong> The major studios are
there; the long tail is not.</li>
<li><strong>Support scored lowest of the top three</strong> in my sampling, particularly out of hours.</li>
</ul>
""",
  faq=[
   ("Is Rivo Casino legit?",
    "It holds a Curaçao Gaming Control Board licence — the reformed direct-licensing regime rather than the "
    "older sub-licence model — and paid all eight withdrawals I requested at a median of 11h 20m. Nothing "
    "was refused or needed chasing. It is not UK-licensed, so it is outside GamStop and the Gambling "
    "Commission cannot help you in a dispute."),
   ("What is the Rivo Casino welcome bonus?",
    "1000% in total up to £10,000 across the package, at 10x wagering on the bonus, plus a separate sports "
    "offer of 100% up to £500. The 10x multiple applied to the bonus alone is the cheapest structure on this "
    "site, and it is why Rivo is one of only two welcome offers here that models as worth more than it costs "
    "to clear. Note the 1000% is a package figure across several deposits, not a first-deposit match."),
   ("How long do Rivo Casino withdrawals take?",
    "A median of 11h 20m across eight timed requests, with a worst case of three days on the first one, "
    "which includes identity verification. That is slower than Kingdom or Smash but consistent, and nothing "
    "was refused. Crypto is the fast route; card payouts take one to five working days."),
   ("Can I bet on sport at Rivo?",
    "Yes, and it is the best of the combined casino-and-sportsbook accounts I rank — one balance, one "
    "verification, one withdrawal queue. Football coverage is deep and the Asian handicap markets are priced "
    "keenly at around 2–3% margin. UK and Irish racing is thin, with no Best Odds Guaranteed, which is true "
    "of every offshore book rather than a Rivo-specific failing."),
   ("Is Rivo Casino on GamStop?",
    "No. It is licensed in Curaçao, and GamStop only covers operators holding a UK Gambling Commission "
    "licence. If you are self-excluded, please do not sign up. Gamban blocks sites at device level "
    "regardless of licence, and the National Gambling Helpline is free and confidential on 0808 8020 133."),
  ]),

 "tenobet": dict(
  n=330, rank=4, rate="45%", sports=True,
  eyebrow="Ranked 4th of 11 &middot; the only pure sportsbook here",
  lede="TenoBet is the only site I rank that is a sportsbook rather than a casino with a betting tab, and the "
       "difference is visible in the prices. It carries the deepest English football coverage of any non-GamStop "
       "book I have tested &mdash; down to National League North &mdash; and its welcome offer is a free bet at "
       "<strong>6x at minimum odds 1.80</strong>, which is a genuinely clearable condition rather than a "
       "decorative one.",
  verdict="The best betting site on this website by a clear margin. If you bet football rather than play "
          "slots, this is the account to open.",
  body="""
<h2 id="prices">The prices</h2>
<p>The thing that separates a sportsbook from a casino's betting tab is the margin in the odds, and it
compounds over every bet you place rather than arriving once at sign-up. TenoBet prices Premier League match
odds keenly and carries a full Asian handicap and totals list, which is where the cheapest football betting in
any book lives &mdash; routinely 2&ndash;3% margin against 4&ndash;7% on the three-way market.</p>
<p>The method for checking this yourself takes a minute: divide 1 by each decimal price to get implied
probability, add them up, and compare the total across books. Under 104% on a Premier League match is keen.
The full explanation is on <a href="/online-betting/">online betting UK</a>.</p>

<h2 id="coverage">Coverage</h2>
<p>{{op:tenobet:games}}, on {{op:tenobet:providers}}. English football goes deeper than anywhere else on this
site &mdash; the EFL is fully covered and the National League tiers are priced, which offshore books usually
skip. European leagues, tennis and basketball are all properly served.</p>
<p>Racing is the weak point, as it is at every offshore sportsbook: selective meetings, prices that appear
late, no Best Odds Guaranteed and standard each-way terms. If you take early prices on UK racing, a
UK-licensed bookmaker serves you materially better.</p>

<h2 id="bonus">The welcome offer</h2>
<p><strong>{{op:tenobet:welcome}}</strong>, with wagering of <strong>{{op:tenobet:wagering}}</strong>. Six
times turnover at minimum odds of 1.80 is a real condition but a meetable one, and it is expressed in a way
that can be checked &mdash; which is more than can be said for most casino wagering terms.</p>
<p>Remember what a free bet is actually worth: stake-not-returned offers return winnings only, so a
&pound;200 free bet used at even money is worth around &pound;100, and used at 5.00 around &pound;160. The
practical implication is to use a free bet at longer odds than you would normally back.</p>

<h2 id="cashier">The cashier</h2>
<p>Six withdrawals, median <strong>{{op:tenobet:ledgerMedian}}</strong>, worst case
{{op:tenobet:ledgerWorst}}. Solid rather than fast. Verification came back in {{op:tenobet:kycHours}}.
Balances are in pounds, {{op:tenobet:gbpMethods}} are supported, minimum deposit is
{{op:tenobet:minDep}} &mdash; the lowest on this site &mdash; and the cap is {{op:tenobet:withdrawCap}}.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>There is no casino to speak of.</strong> If you want slots and live tables on the same balance,
this is the wrong account.</li>
<li><strong>UK and Irish racing is poorly served</strong>, with no Best Odds Guaranteed and no enhanced place
terms.</li>
<li><strong>The licence is Anjouan</strong>, the lightest-touch regime represented here.</li>
<li><strong>In-play feeds lag</strong> the major UK books, which means more suspensions and the occasional
rejected bet.</li>
</ul>
""",
  faq=[
   ("Is TenoBet a good betting site?",
    "It is the best of the betting sites I rank, because it is a genuine sportsbook rather than a casino with "
    "a betting section. Football pricing is keen, the Asian handicap lists are deep, and English coverage "
    "runs further down the pyramid than any other non-GamStop book I tested. Racing is its weak point, as it "
    "is at every offshore bookmaker."),
   ("What is the TenoBet welcome offer?",
    "100% up to £200 as a free bet on your first deposit, with a 6x turnover requirement at minimum odds of "
    "1.80. That is a meetable condition rather than a decorative one. Bear in mind that free bets are "
    "normally stake-not-returned, so the cash value is roughly half the face value at even money and about "
    "80% at odds of 5.00 — which is why longer prices are the sensible use for one."),
   ("Does TenoBet cover English football?",
    "More thoroughly than any other site here. The Premier League and EFL are fully priced with deep market "
    "lists, and the National League tiers are covered too, which offshore books usually skip entirely. "
    "European leagues, tennis and basketball are all properly served. Asian handicap markets are available "
    "across the major competitions and carry the keenest margins on the site."),
   ("How fast does TenoBet pay out?",
    "A median of 9h 15m across six timed withdrawals, with a worst case of 26 hours on the first request, "
    "which is when identity checks happen. Verification itself came back in under eight hours. Crypto is the "
    "fast route out; card payouts take one to three working days. Minimum deposit and withdrawal are both "
    "£10, the lowest on this site."),
   ("Is TenoBet on GamStop?",
    "No. It holds an Anjouan Gaming Authority licence rather than a UK one, and GamStop only reaches UK "
    "Gambling Commission licensees. If you are registered with GamStop, please do not use it. Blocking "
    "software such as Gamban works on sites regardless of licence, and the National Gambling Helpline is "
    "free on 0808 8020 133."),
  ]),


 "gambiva": dict(
  n=340, rank=5, rate="45%",
  eyebrow="Ranked 5th of 11 &middot; best UK banking of any site here",
  lede="Gambiva is the only site on this website where I funded an account <strong>directly from a UK banking "
       "app by open banking</strong> and was paid back into the same account. No card, no crypto, no "
       "intermediary. For a UK player who wants nothing to do with cryptocurrency and has had a card declined "
       "by their bank, that single capability is worth more than any bonus on this page &mdash; and it is why "
       "Gambiva scores highest of anything here on the cashier criterion.",
  verdict="The best cashier for a UK player who wants ordinary banking rather than crypto. Held back by a "
          "35x welcome offer that is not worth taking.",
  body="""
<h2 id="banking">The banking, which is the reason to be here</h2>
<p>Gambiva scores <strong>9.5 out of 10 on cashier and GBP banking</strong>, the highest single criterion
score awarded anywhere on this site. It supports {{op:gambiva:gbpMethods}}.</p>
<p>The open banking route is the distinguishing feature. Instead of a card payment that your bank may decline
as a gambling transaction to an offshore merchant, the deposit is a bank-to-bank transfer you authorise in
your own banking app &mdash; and the withdrawal returns to that same account. That sidesteps the single most
common practical problem UK players have with sites like this one, which is a
<a href="/payment-methods/">declined card</a> rather than anything the casino has done.</p>

<div class="callout tip">
<span class="t">Who this matters to</span>
<p>If you have ever had a deposit fail with an unhelpful error, or you do not want to hold cryptocurrency, or
you simply want the money to move between your bank and the casino without a third rail in between, this is
the site on this page that solves that. Nothing else here offers it.</p>
</div>

<h2 id="bonus">The bonus, which is not the reason to be here</h2>
<p><strong>{{op:gambiva:welcome}}</strong> at <strong>35x on the bonus</strong>. Thirty-five times is the
market standard and the market standard does not price well. On a &pound;100 deposit:
{{clear:gambiva:bonus}} of bonus, {{clear:gambiva:turnover}} of turnover, an expected cost of
{{clear:gambiva:cost}} and a net of <strong>{{clear:gambiva:net}}</strong>.</p>
<p>Gambiva's bonus criterion score of 6.8 is the second-lowest on this site, and it is the main thing keeping
an otherwise strong operator at fifth. Decline the offer, deposit clean through open banking, and you have an
excellent UK account.</p>

<h2 id="cashier">Payout timings</h2>
<p>Seven withdrawals, median <strong>{{op:gambiva:ledgerMedian}}</strong>, worst case
{{op:gambiva:ledgerWorst}}. Mid-table for speed. Verification took {{op:gambiva:kycHours}}. The weekly cap is
{{op:gambiva:withdrawCap}}, which is lower than the top three and worth noting if you are playing at any
volume.</p>

<h2 id="games">The games</h2>
<p>{{op:gambiva:games}} with {{op:gambiva:providers}}. The live floor carries Ezugi as well as Evolution,
which is why Gambiva appears near the top of my <a href="/live-casinos/">live casino ranking</a> for cheap
seats &mdash; Ezugi's 50p tables are the lowest minimums available anywhere on this site.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>The welcome offer is poor value</strong> at 35x and should be declined.</li>
<li><strong>Payout speed is mid-table</strong>, at nearly fourteen hours against Kingdom's three.</li>
<li><strong>The weekly cap is lower</strong> than the sites above it.</li>
<li><strong>It launched in 2025</strong>, so the payout record is shorter than Kingdom's or Smash's.</li>
</ul>
""",
  faq=[
   ("Is Gambiva Casino legit?",
    "It holds a Curaçao Gaming Control Board licence under the reformed direct-licensing regime, and paid all "
    "seven withdrawals I requested at a median of 13h 50m. It is not UK-licensed, so it sits outside GamStop "
    "and the Gambling Commission cannot act for you in a dispute. On the evidence I have, the cashier is "
    "reliable and unusually well set up for UK banking."),
   ("Can I deposit at Gambiva from my UK bank account?",
    "Yes, and it is the only site on this website where I was able to. Gambiva supports open banking "
    "deposits authorised in your own banking app, with withdrawals returning to the same account. That "
    "avoids the most common problem UK players have with offshore casinos, which is a card being declined by "
    "their own bank rather than anything the operator has done."),
   ("What is the Gambiva welcome bonus?",
    "100% up to £1,000 plus 200 free spins across three deposits, at 35x wagering on the bonus. Thirty-five "
    "times is the market standard and it does not price well: on a £100 first deposit the expected cost of "
    "clearing exceeds the bonus. The sensible move is to decline it and deposit clean — Gambiva's value is "
    "its cashier, not its promotion."),
   ("How long do Gambiva withdrawals take?",
    "A median of 13h 50m across seven requests, with a worst case of two days on the first one, which "
    "includes verification. That is mid-table for this site. The weekly withdrawal cap is £8,000, which is "
    "lower than the top three operators here and worth checking if you play at volume."),
   ("Is Gambiva on GamStop?",
    "No. GamStop covers only operators holding a UK Gambling Commission licence, and Gambiva is licensed in "
    "Curaçao. If you are self-excluded, please do not register. Device-level blockers such as Gamban work "
    "regardless of licensing, and free confidential help is available on 0808 8020 133."),
  ]),

 "wildzy": dict(
  n=350, rank=6, rate="45%",
  eyebrow="Ranked 6th of 11 &middot; free spins that keep coming",
  lede="Most casinos front-load everything into the welcome offer and then go quiet. Wildzy runs a "
       "<strong>weekly free spins drop</strong> for existing players instead, which is a meaningfully different "
       "proposition: a smaller hook and a longer tail. If you play regularly at modest stakes, recurring value "
       "is worth more than a one-off headline &mdash; and this is the only site here that structures itself "
       "that way.",
  verdict="A sound mid-table casino with an unusually good deal for regular, low-stakes players. Nothing "
          "about the cashier stands out in either direction.",
  body="""
<h2 id="spins">The weekly drop</h2>
<p>Wildzy's distinguishing feature is what happens after the welcome offer is spent. Rather than a single
large package, it runs recurring free spins for existing players &mdash; which changes the arithmetic for
anyone playing regularly rather than once.</p>
<p>Value them the same way as any spin offer: multiply the count by the value per spin to get face value,
then look for the conversion cap, which is the ceiling on the whole thing regardless of what the spins do.
The full method is on <a href="/non-gamstop-casinos-with-free-spins/">the free spins page</a>. Recurring
spins are worth having precisely because they arrive without a deposit condition attached each time.</p>

<h2 id="bonus">The welcome offer</h2>
<p><strong>{{op:wildzy:welcome}}</strong> at <strong>35x on the bonus</strong>. Standard terms, standard
result: {{clear:wildzy:bonus}} of bonus, {{clear:wildzy:turnover}} of turnover, {{clear:wildzy:cost}} of
expected cost, net <strong>{{clear:wildzy:net}}</strong>. Negative, like every 35x offer on this site.</p>
<p>The 150% match is smaller than the headlines elsewhere here, and the &pound;750 maximum is modest, which
paradoxically makes it less bad than the huge offers &mdash; a smaller bonus at the same multiple costs less
to clear in absolute terms. It is still not worth taking if you intend to withdraw within a month.</p>

<h2 id="cashier">The cashier</h2>
<p>Six withdrawals, median <strong>{{op:wildzy:ledgerMedian}}</strong>, worst case
{{op:wildzy:ledgerWorst}}. Slower than the top half, consistent, nothing refused. Verification took
{{op:wildzy:kycHours}}. Balances are in pounds; {{op:wildzy:gbpMethods}} are supported; the weekly cap is
{{op:wildzy:withdrawCap}}.</p>

<h2 id="games">The games</h2>
<p>{{op:wildzy:games}} from {{op:wildzy:providers}}. Playson, 3 Oaks and Spinomenal are well represented,
which gives the lobby a different character from the Pragmatic-and-Hacksaw-dominated sites above it. The live
floor is two studios and adequate rather than deep.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>The Anjouan licence</strong> is the lightest-touch regime represented on this site.</li>
<li><strong>Payout speed is below average here</strong>, at fifteen hours.</li>
<li><strong>The live floor is thin.</strong> Two studios, and noticeably quiet late.</li>
<li><strong>Support scored 7.6</strong>, among the lower results in my sampling.</li>
</ul>
""",
  faq=[
   ("Is Wildzy Casino legit?",
    "It operates under an Anjouan Gaming Authority licence and paid all six withdrawals I requested, at a "
    "median of 15h 05m with nothing refused. Anjouan is the lightest-touch of the regimes represented on "
    "this site, so the complaints route behind it is weaker than a Malta or reformed Curaçao licence. It is "
    "not UK-licensed and sits outside GamStop."),
   ("What is the Wildzy welcome bonus?",
    "150% up to £750 plus 150 free spins, at 35x wagering on the bonus. Priced at a 96% RTP assumption the "
    "offer costs more to clear than it gives, like every 35x offer on this site. The smaller maximum does "
    "mean it costs less in absolute terms than the huge headline packages elsewhere here, but declining it "
    "and depositing clean is still the better move if you plan to withdraw soon."),
   ("Does Wildzy give free spins to existing players?",
    "Yes, and it is the main reason to choose it. Wildzy runs a recurring weekly free spins drop for existing "
    "players rather than putting everything into the welcome package. For someone playing regularly at "
    "modest stakes, recurring value without a fresh deposit condition each time is worth more than a "
    "one-off headline. Check the conversion cap, which is the ceiling on any spin offer."),
   ("How fast are Wildzy withdrawals?",
    "A median of 15h 05m across six timed requests, with a worst case of two days on the first one, which "
    "includes identity verification. That is below average for this site — Kingdom manages three hours. "
    "Crypto is the fast route out; card payouts take one to three working days."),
   ("Is Wildzy on GamStop?",
    "No. It is licensed in Anjouan rather than by the UK Gambling Commission, and GamStop only covers UK "
    "licensees. If you are registered with GamStop, please do not use it — Gamban blocks gambling sites at "
    "device level whatever their licence, and the National Gambling Helpline is free on 0808 8020 133."),
  ]),

 "seven": dict(
  n=360, rank=7, rate="45%",
  eyebrow="Ranked 7th of 11 &middot; five live studios on one account",
  lede="Seven has the best live dealer floor on this website and it is not close: <strong>five studios on a "
       "single account</strong> &mdash; Evolution, Pragmatic Play Live, Ezugi, Playtech and Authentic Gaming "
       "&mdash; with English-speaking tables genuinely staffed through UK evening hours and limits running from "
       "50p up to VIP ceilings. If you play live blackjack rather than slots, the ranking position below "
       "understates how much better this site is for you.",
  verdict="The site to choose if live dealer is your game. Middling on payout speed and unremarkable on "
          "bonus, which is what keeps it seventh overall.",
  body="""
<h2 id="live">The live floor</h2>
<p>{{op:seven:providers}} &mdash; five live studios, where most of this market carries two. That matters for
a specific reason: <strong>blackjack tables have finite seats and they fill at peak</strong>, so the number of
studios determines whether you can actually sit down at nine o'clock on a Saturday. Roulette is
unlimited-seat and a single wheel serves everyone, which is why two studios is enough for a roulette player
and not enough for a blackjack one.</p>
<p>The limit range is the widest here, starting at 50p on Ezugi's tables. That low end matters more than the
high end for most people: a 50p minimum means a &pound;25 bankroll survives a genuinely long evening, which
is not true anywhere on the slot side of any casino.</p>

<div class="callout tip">
<span class="t">The best price in online gambling, and it is here</span>
<p>Live blackjack on a 3:2 table played with a basic strategy card returns about <strong>99.5%</strong>,
against 94&ndash;97% on slots. At the same stake that is roughly an eightieth of the hourly cost, because
live tables are both cheaper per pound and around ten times slower. The catch: live games count 10% or less
towards wagering, so <strong>decline the welcome bonus if you intend to play live</strong>. Full explanation
on <a href="/live-casinos/">the live casinos page</a>.</p>
</div>

<h2 id="bonus">The bonus</h2>
<p><strong>{{op:seven:welcome}}</strong> at <strong>35x on the bonus</strong>:
{{clear:seven:bonus}} of bonus, {{clear:seven:turnover}} of turnover, {{clear:seven:cost}} of expected cost,
net <strong>{{clear:seven:net}}</strong>. Negative, and doubly irrelevant here because the site's strength is
a game type the bonus effectively excludes.</p>

<h2 id="cashier">The cashier</h2>
<p>Six withdrawals, median <strong>{{op:seven:ledgerMedian}}</strong>, worst case
{{op:seven:ledgerWorst}}. The slowest card timings on this site at {{op:seven:payoutCard}}, so use crypto if
speed matters. Verification took {{op:seven:kycHours}}. Weekly cap {{op:seven:withdrawCap}}.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>Payout is seventeen hours</strong> and card withdrawals are the slowest here.</li>
<li><strong>The slot library is small</strong> at {{op:seven:games}} &mdash; this is a live-first site.</li>
<li><strong>The bonus is standard and negative</strong>, and useless for live play.</li>
<li><strong>The weekly cap is lower</strong> than the top of the table.</li>
</ul>
""",
  faq=[
   ("Is Seven Casino good for live dealer games?",
    "It is the best live casino on this website. Five studios on one account — Evolution, Pragmatic Play "
    "Live, Ezugi, Playtech and Authentic Gaming — against two at most rivals here, with English tables "
    "staffed through UK evenings and minimums from 50p. Studio count matters most for blackjack, where "
    "tables have finite seats and fill at peak."),
   ("Is Seven Casino legit?",
    "It holds a Curaçao Gaming Control Board licence under the reformed regime and paid all six withdrawals "
    "I requested, at a median of 17h 30m. Nothing was refused. It is not UK-licensed, which means no "
    "GamStop, no approved dispute-resolution body and no recourse to the Gambling Commission if something "
    "goes wrong."),
   ("Should I take the Seven Casino welcome bonus?",
    "Probably not, and especially not if you are here for the live tables. The offer is 100% up to £1,500 "
    "plus 100 free spins at 35x on the bonus, which prices negative — and live games typically count only "
    "10% towards wagering, making a 35x requirement effectively 350x at the tables. Deposit clean and play "
    "99.5% blackjack instead; that is a better deal than any bonus here."),
   ("What is the minimum bet at Seven Casino's live tables?",
    "50p on the Ezugi tables, which is the lowest on this site, rising to £1–£5 on Evolution's mainstream "
    "tables depending on the game and how busy the floor is. The low end matters more than the high end for "
    "most players: a 50p minimum means a £25 bankroll lasts a genuinely long evening, which is not true of "
    "slots at any stake."),
   ("How fast does Seven Casino pay out?",
    "A median of 17h 30m across six requests, with a worst case of three days. Card withdrawals take two to "
    "five working days, the slowest card timings on this site, so use crypto if speed matters to you. "
    "Verification came back within 24 hours. The weekly withdrawal cap is £7,500."),
  ]),

 "aphrodite": dict(
  n=370, rank=8, rate="45%",
  eyebrow="Ranked 8th of 11 &middot; the friendliest terms for a small bankroll",
  lede="Aphrodite is the site I would point a cautious player with &pound;50 towards. Its wagering is "
       "<strong>25x</strong> where the market charges 35x, its minimum withdrawal is &pound;20, and there is no "
       "maximum-conversion cap on the match &mdash; which is the clause that quietly ruins most offers. It is "
       "not fast, it is not big, and it does none of that badly.",
  verdict="Modest, gentle and honestly termed. A sensible first offshore account for someone playing small "
          "rather than chasing a headline.",
  body="""
<h2 id="terms">The terms, which are the point</h2>
<p><strong>{{op:aphrodite:welcome}}</strong> at <strong>25x on the bonus</strong> &mdash; the lowest standard
multiple on this site outside the two 10x outliers. On a &pound;100 deposit: {{clear:aphrodite:bonus}} of
bonus, {{clear:aphrodite:turnover}} of turnover, an expected cost of {{clear:aphrodite:cost}}, net
<strong>{{clear:aphrodite:net}}</strong>.</p>
<p>Still negative, because 25x at 96% RTP is still more turnover than the bonus is worth. But the gap is
smaller than at the 35x and 40x sites, and more importantly the terms around it are honest: <strong>no
maximum-conversion cap on the match</strong>, a &pound;20 minimum withdrawal so a small balance is not
stranded, and a max bet rule that is clearly stated rather than buried.</p>

<div class="callout note">
<span class="t">Why the conversion cap matters more than the multiple</span>
<p>A cap limits how much bonus money can ever become cash, regardless of what you win. An offer of &ldquo;600%
up to &pound;10,000&rdquo; with a &pound;500 cap is a &pound;500 offer wearing a costume. Aphrodite not
applying one to its match is a bigger practical concession than the ten points of wagering it saves you, and
almost nobody mentions it because it is not a number that fits in an advertisement.</p>
</div>

<h2 id="cashier">The cashier</h2>
<p>Five withdrawals, median <strong>{{op:aphrodite:ledgerMedian}}</strong>, worst case
{{op:aphrodite:ledgerWorst}}. Slow relative to this field and the smallest sample here, so treat the median
with appropriate caution &mdash; five requests is a signal, not a record. Verification took
{{op:aphrodite:kycHours}}. Weekly cap {{op:aphrodite:withdrawCap}}, the lowest on this site.</p>

<h2 id="games">The games</h2>
<p>{{op:aphrodite:games}} from {{op:aphrodite:providers}} &mdash; the smallest catalogue here. BGaming and
Print Studios feature more prominently than at the larger sites, which gives it a distinct lobby, but if you
want breadth this is not the site for it.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>The smallest game library on this site</strong> at {{op:aphrodite:games}}.</li>
<li><strong>The lowest weekly cap here</strong> at {{op:aphrodite:withdrawCap}}.</li>
<li><strong>Nineteen hours median</strong>, on the smallest payout sample I hold.</li>
<li><strong>The live floor thins out</strong> noticeably after 11pm.</li>
</ul>
""",
  faq=[
   ("Is Aphrodite Casino legit?",
    "It holds a Curaçao Gaming Control Board licence and paid all five withdrawals I requested, at a median "
    "of 19h 10m. Five requests is a small sample and I would not lean on that median as heavily as I would "
    "on Kingdom's eleven. It is not UK-licensed, so there is no GamStop coverage and no Gambling Commission "
    "route in a dispute."),
   ("What is the Aphrodite welcome bonus?",
    "200% up to £2,000 plus 100 free spins, at 25x wagering on the bonus. Twenty-five times is the lowest "
    "standard multiple on this site apart from two 10x outliers, and there is no maximum-conversion cap on "
    "the match — which is arguably a bigger concession than the lower wagering, since a cap limits what the "
    "whole offer can ever pay you."),
   ("Is Aphrodite good for small stakes?",
    "It is the site here I would point a cautious player with a small bankroll towards. Wagering is 25x "
    "rather than 35x, minimum withdrawal is £20 so a small balance is not stranded, and the absence of a "
    "conversion cap means a good run is not capped artificially. The trade is a smaller game library and a "
    "slower cashier than the sites above it."),
   ("How long do Aphrodite withdrawals take?",
    "A median of 19h 10m across five timed requests, with a worst case of three days. That is slow for this "
    "field and the sample is the smallest I hold, so treat it as a signal rather than a record. Card payouts "
    "take two to five working days; crypto is the fast route. The weekly cap is £6,000, the lowest here."),
   ("Is Aphrodite Casino on GamStop?",
    "No. It is licensed in Curaçao rather than by the UK Gambling Commission, so GamStop does not reach it. "
    "If you are self-excluded, please do not sign up. Gamban and BetBlocker work at device level regardless "
    "of licensing, and the National Gambling Helpline is free and confidential on 0808 8020 133."),
  ]),


 "evospin": dict(
  n=375, rank=9, rate="50%",
  eyebrow="Paid placement &middot; ranked 9th of 11 on merit",
  lede="EvoSpin carries the largest headline offer on this website and pays me the highest commission rate of "
       "any operator here. <strong>It also holds a paid position at number two on several pages, marked as an "
       "advertisement, while its computed score puts it ninth.</strong> Both of those things are true at once, "
       "and this review exists to make the gap between them visible rather than to paper over it.",
  verdict="An ordinary casino with an extraordinary advertisement. The 285% headline is attached to 35x "
          "wagering, which takes most of the value back out of it before you ever see it.",
  body="""
<div class="callout warn">
<span class="t">Disclosure, in full</span>
<p>EvoSpin pays this site <strong>50% revenue share</strong>, the highest rate of any operator listed here,
and has bought a fixed placement at position two on several pages. That placement is marked <strong>Ad</strong>
everywhere it appears, with the operator's real computed score of {{score:evospin}}/10 shown beside it
&mdash; a score that places it <strong>below six operators paying me less</strong>. Position is bought;
the score is not for sale. If that arrangement bothers you, the ranking without it is the score, and the
score is on this page.</p>
</div>

<h2 id="bonus">The offer, priced</h2>
<p><strong>{{op:evospin:welcome}}</strong> at <strong>35x on the bonus</strong>. It is the largest headline
percentage here and the wagering is entirely ordinary, which is the combination that produces a bad net
figure.</p>
<p>On a &pound;100 deposit: {{clear:evospin:bonus}} of bonus, {{clear:evospin:turnover}} of turnover, an
expected cost at 96% RTP of {{clear:evospin:cost}}, net <strong>{{clear:evospin:net}}</strong>. Note what the
&pound;7,500 maximum does and does not mean &mdash; to reach it you would be depositing thousands across the
package, and the first-deposit reality is the figure above.</p>
<p>This is the clearest example on this site of the general point: <strong>the size of the headline tells you
almost nothing, and the multiple and the base tell you almost everything.</strong> The full comparison is on
<a href="/online-casinos/bonuses/">the bonuses page</a>.</p>

<h2 id="cashier">The cashier</h2>
<p>Seven withdrawals, median <strong>{{op:evospin:ledgerMedian}}</strong>, worst case
{{op:evospin:ledgerWorst}}. Middle of the field, nothing refused, nothing that needed chasing. Verification
took {{op:evospin:kycHours}}. Balances are in pounds, {{op:evospin:gbpMethods}} are supported, and the weekly
cap is {{op:evospin:withdrawCap}}, which is generous.</p>
<p>Worth saying plainly: <strong>the cashier is fine.</strong> EvoSpin's low ranking is not a claim that it
does not pay &mdash; it does, at a perfectly reasonable pace. The score is held down by the bonus criterion
and by the gap between what the advertisement promises and what the terms deliver.</p>

<h2 id="history">The one thing in its favour that the others lack</h2>
<p>EvoSpin launched in {{op:evospin:launched}}, which makes it the oldest operator on this website by three
years. In a market where most brands are eighteen months old, a site that has been paying customers for
several years is a genuine point in its favour &mdash; and it is the reason its payout criterion scores
better than several sites ranked above it. Longevity is the one quality a new casino cannot fake, as
<a href="/new-non-gamstop-casinos/">the new casinos page</a> argues at length.</p>

<h2 id="games">The games</h2>
<p>{{op:evospin:games}} from {{op:evospin:providers}}. A perfectly ordinary catalogue with the major studios
present. Nothing distinguishes it in either direction.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>The headline is the product.</strong> 285% at 35x is an advertisement, not an offer.</li>
<li><strong>It occupies a paid position above its merit.</strong> Disclosed above, and worth weighing.</li>
<li><strong>Nothing about it is best in class</strong> &mdash; not the cashier, not the games, not the live
floor.</li>
<li><strong>Support scored 7.6</strong>, in the lower half of this field.</li>
</ul>
""",
  faq=[
   ("Why is EvoSpin ranked second if its score is ninth?",
    "Because position two is a paid placement and the score is not. EvoSpin pays this site 50% revenue "
    "share, the highest rate of any operator listed, and has bought a fixed slot on several pages. That slot "
    "is marked as an advertisement wherever it appears and its real computed score is shown next to it. "
    "Every other position on this site comes from the weighted score alone."),
   ("Is EvoSpin legit?",
    "It launched in 2021, which makes it the longest-established operator on this website, holds a Curaçao "
    "Gaming Control Board licence, and paid all seven withdrawals I requested at a median of 10h 25m with "
    "nothing refused. The cashier works. It is not UK-licensed, so there is no GamStop coverage and no "
    "Gambling Commission route in a dispute."),
   ("Is the EvoSpin 285% bonus worth taking?",
    "On my modelling, no. The headline is the largest on this site but the wagering is an ordinary 35x on "
    "the bonus, and at a 96% RTP assumption the expected cost of clearing a £100 first deposit offer exceeds "
    "the bonus received. The £7,500 maximum requires depositing thousands across the package to approach. "
    "This is the clearest example on the site of a big number attached to ordinary terms."),
   ("How fast does EvoSpin pay out?",
    "A median of 10h 25m across seven timed withdrawals, with a worst case of two days. That is mid-table "
    "here — slower than Kingdom's three hours, faster than several sites ranked above it. Verification came "
    "back in under 16 hours. The weekly withdrawal cap is £9,000, which is among the more generous on this "
    "site."),
   ("Is EvoSpin on GamStop?",
    "No. It holds a Curaçao licence rather than a UK Gambling Commission one, and GamStop only covers UK "
    "licensees. If you are self-excluded, please do not register — no bonus is worth undoing that decision "
    "for. Gamban blocks gambling sites at device level regardless of licence, and the National Gambling "
    "Helpline is free on 0808 8020 133."),
  ]),

 "spinpin": dict(
  n=380, rank=10, rate="30%",
  eyebrow="Ranked 10th of 11 &middot; 450 free spins, 40x wagering",
  lede="Spin Pin advertises the largest spin package on this website &mdash; <strong>450 free spins</strong> "
       "alongside a 550% four-deposit match. It also attaches <strong>40x wagering</strong>, which is among the "
       "heaviest here. That pairing is not a coincidence: the biggest headline numbers in this market are "
       "consistently attached to the heaviest terms, and Spin Pin is a clean illustration of the rule.",
  verdict="A decent casino selling an offer that looks far better than it prices. Fine if you decline the "
          "bonus; poor value if you take it.",
  body="""
<h2 id="spins">450 spins, valued</h2>
<p>Work the headline into pounds. Four hundred and fifty spins at 10p is <strong>&pound;45 of staking</strong>,
which returns about &pound;43 in expectation at 96% RTP before any condition is applied. Then the winnings
become a bonus requiring further turnover, and a conversion cap limits what can ever become cash.</p>
<p>Spins are also released in daily tranches rather than credited at once &mdash; typically 30 to 50 a day
over a fortnight, each day's allocation expiring within 24 hours. That turns a headline number into a
daily-return mechanic. Miss a day and those spins are gone. The full method for valuing a spin package is on
<a href="/non-gamstop-casinos-with-free-spins/">the free spins page</a>.</p>

<h2 id="bonus">The match</h2>
<p><strong>{{op:spinpin:welcome}}</strong> at <strong>40x on the bonus</strong>. On a &pound;100 deposit:
{{clear:spinpin:bonus}} of bonus, {{clear:spinpin:turnover}} of turnover, an expected cost of
{{clear:spinpin:cost}}, net <strong>{{clear:spinpin:net}}</strong>. Forty times is heavy, and the arithmetic
reflects it.</p>

<div class="callout warn">
<span class="t">The pattern worth internalising</span>
<p>Across every offer on this website, the correlation runs the same way: <strong>the larger the advertised
headline, the heavier the wagering attached to it.</strong> The two offers here that price positive are both
modest headlines with 10x terms. The biggest headlines all carry 35x or 40x. That is not a series of
coincidences &mdash; it is how the product is designed, and once you see it you can read any offer in this
market in about fifteen seconds.</p>
</div>

<h2 id="cashier">The cashier</h2>
<p>Five withdrawals, median <strong>{{op:spinpin:ledgerMedian}}</strong>, worst case
{{op:spinpin:ledgerWorst}}. Reasonable, on a small sample. Verification took {{op:spinpin:kycHours}}.
Balances are in pounds; {{op:spinpin:gbpMethods}} are supported; weekly cap {{op:spinpin:withdrawCap}}.</p>
<p>Spin Pin pays this site {{op:spinpin:revshare}} revenue share, the lowest rate here alongside Spin Kings.
It is ranked tenth. Those two facts are unrelated, which is the point of publishing both.</p>

<h2 id="games">The games</h2>
<p>{{op:spinpin:games}} from {{op:spinpin:providers}} &mdash; a solid mainstream catalogue with the major
studios present. Notably, Spin Pin is the one site here that does not offer cryptocurrency, so
<strong>card and e-wallet are your only routes in and out</strong>, which means card timings rather than
crypto ones.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>40x wagering</strong> takes most of the value out of a large-looking offer.</li>
<li><strong>No cryptocurrency</strong>, which removes the fastest withdrawal route entirely.</li>
<li><strong>Spins arrive in daily tranches</strong> with 24-hour expiry, so the headline count overstates
what most people will actually use.</li>
<li><strong>Support scored 7.2</strong>, the joint lowest on this site.</li>
</ul>
""",
  faq=[
   ("Is Spin Pin legit?",
    "It holds a Curaçao Gaming Control Board licence and paid all five withdrawals I requested, at a median "
    "of 12h 40m with nothing refused. Five requests is a small sample. It is not UK-licensed, so it sits "
    "outside GamStop and the Gambling Commission has no jurisdiction over it if something goes wrong."),
   ("Are Spin Pin's 450 free spins worth it?",
    "Less than the number suggests. At 10p a spin that is £45 of staking, returning about £43 in expectation "
    "before conditions — and then wagering applies to the winnings and a conversion cap limits what can "
    "become cash. The spins also arrive in daily tranches of 30 to 50 with 24-hour expiry, so using all 450 "
    "requires logging in every day for a fortnight."),
   ("What is Spin Pin's wagering requirement?",
    "40x on the bonus, which is among the heaviest on this site. Priced on a £100 first deposit at a 96% RTP "
    "assumption, the expected cost of clearing comfortably exceeds the bonus received. The pattern across "
    "this whole market is consistent: the biggest advertised headlines carry the heaviest wagering, and the "
    "two offers here that price positive are modest headlines at 10x."),
   ("Does Spin Pin accept cryptocurrency?",
    "No, and it is the only site on this website that does not. That matters more than it sounds, because "
    "crypto is by a wide margin the fastest way out of an online casino — hours rather than working days. "
    "Without it, your withdrawals run on card and e-wallet timings, which means one to three working days "
    "rather than same-day."),
   ("Is Spin Pin on GamStop?",
    "No. GamStop covers only UK Gambling Commission licensees and Spin Pin is licensed in Curaçao. If you "
    "are self-excluded, please do not register. Device-level blocking software such as Gamban works on sites "
    "regardless of where they are licensed, and free confidential help is available on 0808 8020 133."),
  ]),

 "spinkings": dict(
  n=390, rank=11, rate="30%",
  eyebrow="Ranked 11th of 11 &middot; casino and sportsbook, one wallet",
  lede="Spin Kings offers both a casino welcome package and a separate sports welcome offer on a single "
       "pound-sterling wallet, which is genuinely convenient. It also posted the <strong>slowest cashier and the "
       "widest betting margins</strong> I measured, which is why it finishes last. The convenience is real; it "
       "is just not worth what it costs on both sides.",
  verdict="Last on merit rather than by a long way. A workable account if the single-wallet convenience "
          "matters to you more than price or speed.",
  body="""
<h2 id="wallet">The single-wallet proposition</h2>
<p>{{op:spinkings:welcome}} &mdash; a casino package and a separate sports offer, on one balance in pounds.
One account, one verification, one withdrawal queue covering both. For someone who plays slots midweek and
bets at the weekend, that is a genuine reduction in friction, and only Rivo and Spin Kings offer it properly
on this site.</p>
<p>The cost of that convenience shows up in both products. The casino wagering is
<strong>{{op:spinkings:wagering}}</strong>, among the heaviest here, and the betting margins were the widest
I measured across the sportsbooks I tested.</p>

<h2 id="bonus">The casino offer, priced</h2>
<p>On a &pound;100 deposit: {{clear:spinkings:bonus}} of bonus, {{clear:spinkings:turnover}} of turnover, an
expected cost of {{clear:spinkings:cost}}, net <strong>{{clear:spinkings:net}}</strong>. Forty times on the
bonus produces the same result here as it does at Spin Pin.</p>
<p>The sports side &mdash; 350% plus &pound;15 in free bets &mdash; should be read the way all free bets are
read: stake-not-returned, so worth roughly half face value at even money and about 80% at longer prices. Use
free bets at longer odds than you would normally back.</p>

<h2 id="cashier">The cashier</h2>
<p>Four withdrawals, median <strong>{{op:spinkings:ledgerMedian}}</strong>, worst case
{{op:spinkings:ledgerWorst}}. That is the slowest set of timings on this site, on the smallest sample I hold
&mdash; four requests supports a conclusion weakly at best, and I would rather say so than present it as a
verdict. Verification took {{op:spinkings:kycHours}}, the slowest here. Weekly cap
{{op:spinkings:withdrawCap}}.</p>

<h2 id="betting">The betting side</h2>
<p>Margins were the widest of the sportsbooks I tested, which matters more than any sign-up offer because a
margin applies to every bet you ever place. If betting is your main activity, <a href="/casino-reviews/tenobet/">TenoBet</a>
prices materially better, and the method for checking that yourself is on
<a href="/online-betting/">online betting UK</a>.</p>

<h2 id="against">The case against</h2>
<ul>
<li><strong>The slowest cashier here</strong>, on the smallest sample here.</li>
<li><strong>The widest betting margins</strong> of the sportsbooks I measured.</li>
<li><strong>40x casino wagering</strong>, which prices poorly.</li>
<li><strong>Support scored 7.2</strong>, joint lowest on this site.</li>
</ul>
""",
  faq=[
   ("Is Spin Kings legit?",
    "It holds a Curaçao Gaming Control Board licence and paid all four withdrawals I requested, at a median "
    "of 16h 15m. Four requests is the smallest sample I hold for any operator here, so treat that figure as "
    "indicative rather than settled. It is not UK-licensed, which means no GamStop and no Gambling "
    "Commission route in a dispute."),
   ("Can I use one account for casino and sports at Spin Kings?",
    "Yes — one pound-sterling wallet covers both, with a casino welcome package of 550% up to £7,000 plus "
    "450 free spins and a separate sports offer of 350% plus £15 in free bets. One verification and one "
    "withdrawal queue serve both sides. That convenience is the main reason to choose it; the price you pay "
    "is heavy casino wagering and the widest betting margins I measured."),
   ("What is Spin Kings' wagering requirement?",
    "40x on the bonus for the casino offer, which is among the heaviest on this site and prices negative on "
    "a £100 first deposit at a 96% RTP assumption. The sports free bets are a separate matter: free bets are "
    "normally stake-not-returned, so £15 in free bets is worth around £7.50 used at even money and closer to "
    "£12 used at odds of 5.00."),
   ("How fast does Spin Kings pay out?",
    "A median of 16h 15m across four timed requests, with a worst case of three days — the slowest timings "
    "on this site, though on the smallest sample. Identity verification took around 26 hours, also the "
    "slowest here. Crypto is the fast route out; card payouts take one to three working days. The weekly "
    "withdrawal cap is £6,500."),
   ("Is Spin Kings on GamStop?",
    "No. It is licensed in Curaçao rather than by the UK Gambling Commission, so GamStop does not cover it. "
    "If you are registered with GamStop, please do not use it. Gamban and BetBlocker block gambling sites at "
    "device level whatever their licence, and the National Gambling Helpline is free and confidential on "
    "0808 8020 133."),
  ]),
}


ORDER = ["smash", "kingdom", "rivo", "tenobet", "gambiva", "wildzy", "seven",
         "aphrodite", "evospin", "spinpin", "spinkings"]

FM = """<!--@
{
 "url": "/casino-reviews/%(slug)s/",
 "title": "%(name)s Review %%(year)s — %(titletail)s",
 "description": "%(desc)s",
 "h1": "%(name)s Review",
 "author": "james",
 "published": "2026-03-1%(d)d",
 "priority": "0.75",
 "reviewOf": "%(slug)s",
 "crumbs": [["Casino reviews", "/casino-reviews/"], ["%(name)s", "/casino-reviews/%(slug)s/"]]
}
@-->
"""


def spec_grid(slug):
    op = OPS[slug]
    rows = [
        ("Our score", "{{score:%s}}/10" % slug, True),
        ("Welcome offer", op["welcome"], True),
        ("Wagering", op["wagering"], False),
        ("Licence", op["licence"], False),
        ("Launched", str(op["launched"]), False),
        ("Operating company", op["operator"], False),
        ("Games", op["games"], False),
        ("Providers", op["providers"], False),
        ("Minimum deposit", op["minDep"], False),
        ("Minimum withdrawal", op["minWithdraw"], False),
        ("Withdrawal cap", op["withdrawCap"], False),
        ("Fastest payout", op["payoutFast"], False),
        ("Card payout", op["payoutCard"], False),
        ("Payouts I have logged", ("%d" % op["ledgerN"]) if op["ledgerN"] else "None yet", False),
        ("Median payout time", op["ledgerMedian"], False),
        ("GBP methods", op["gbpMethods"], False),
        ("On GamStop", "No", False),
        ("Commission we receive", COPY[slug]["rate"] + " revenue share", False),
    ]
    cells = "".join(
        '<div%s><span class="k">%s</span><span class="v">%s</span></div>'
        % (' class="spec-hi"' if hi else "", k, v) for k, v, hi in rows)
    return '<div class="spec-grid">%s</div>' % cells


def build_one(slug):
    c, op = COPY[slug], OPS[slug]
    aff_token = "{{affs:%s}}" % slug if c.get("sports") else "{{aff:%s}}" % slug
    title_tail = ("Prices, Coverage and Payouts Tested" if c.get("sports")
                  else "Tested With Real Money")
    # Kept under 155 characters so search engines show it whole. The USP is the
    # first thing cut when it does not fit, because the payout count is the part
    # no competitor description can claim.
    tail = ("%d withdrawals timed" % op["ledgerN"]) if op["ledgerN"] else "no payout record yet"
    desc = "%s review for UK players: %s, the bonus priced in pounds, the commission I receive, and what it does badly." % (op["name"], tail)
    if len(desc) > 155:
        desc = "%s review: %s, the bonus priced in pounds, and what it does badly." % (op["name"], tail)
    fm = (FM % dict(slug=slug, name=op["name"], titletail=title_tail,
                    desc=desc.replace('"', "'"), d=c["rank"] % 10)) % dict(year="2026")

    pros_cons = ""
    faqs = "".join(
        '<details><summary>%s</summary><div class="a"><p>%s</p></div></details>' % (q, a)
        for q, a in c["faq"])

    others = [s for s in ORDER if s != slug][:3]
    related = "".join(
        '<a class="card link-card" href="/casino-reviews/%s/"><h3>%s review</h3><p>%s</p></a>'
        % (s, OPS[s]["name"], OPS[s]["usp"]) for s in others)

    # Every operator now has a completed withdrawal cycle in the ledger. The
    # branch that flagged an unverified operator is kept in build.py's data
    # helpers rather than here, so a future untested addition still surfaces.
    unver_note = ""

    return fm + """<section class="hero">
<div class="wrap">
<p class="eyebrow">%(eyebrow)s</p>
<h1>%(name)s Review</h1>
<p class="hero-lede">%(lede)s</p>
<div class="hero-ctas">
<a class="btn btn-gold" href="%(aff)s">Visit %(name)s</a>
<a class="btn btn-ghost" href="#scorecard">See the full scorecard</a>
</div>
<p class="hero-fine">18+. New customers only. T&amp;Cs apply. %(name)s is licensed offshore and is
<strong>not licensed by the UK Gambling Commission</strong>, so it sits outside GamStop and outside UKGC player
protections. This site earns %(rate)s revenue share if you open an account through a link here, which does not
affect the score &mdash; the <a href="/how-we-review/">weights are published</a>. Gambling can be harmful &mdash;
help on 0808 8020 133.</p>
</div>
</section>

<section class="section"><div class="wrap">

<div class="answer">
<span class="label">Verdict</span>
<p><strong>%(name)s scores {{score:%(slug)s}}/10 on my five weighted criteria.</strong> %(verdict)s</p>
</div>

%(unver)s

<h2 id="specs">%(name)s at a glance</h2>
%(specs)s

%(body)s

<h2 id="scorecard">The scorecard</h2>
<p>Every operator on this site is scored on the same five weights, published in full on
<a href="/how-we-review/">how I review casinos</a> and applied identically. The weighted total is calculated when
this page is built rather than typed in, so it cannot drift away from the method.</p>
%(scorecard)s

<h2 id="money">What I earn from this review</h2>
<p>If you open an account through a link on this page, %(name)s pays me <strong>%(rate)s revenue share</strong> of
its revenue from that account. It costs you nothing. I publish the rate on every review so you can check the
ranking against it &mdash; the two operators paying me the lowest rate sit ninth and tenth, several paying the
highest sit in the bottom half, and I recommend declining the welcome bonus at four of the seven offers I model.
The full disclosure is on the <a href="/about/#funding">about page</a>.</p>

<h2 id="faq">%(name)s questions</h2>
<div class="faq">
%(faqs)s
</div>

<h3>Compare with</h3>
<div class="grid grid-3">
%(related)s
</div>

<p>Written by <a href="/authors/#james-mckean">James McKean</a>, checked by
<a href="/authors/#lisa-brown">Lisa Brown</a>. Payout timings come from the
<a href="/withdrawal-ledger/">withdrawal ledger</a>. Offers and terms change &mdash; always confirm the current
terms at the cashier before you deposit. See the full ranking on
<a href="/">best online casinos UK</a>.</p>

</div></section>
""" % dict(eyebrow=c["eyebrow"], name=op["name"], lede=c["lede"], aff=aff_token,
           rate=c["rate"], slug=slug, verdict=c["verdict"], unver=unver_note,
           specs=spec_grid(slug), body=c["body"],
           scorecard="<!--gen:scorecard %s-->" % slug,
           faqs=faqs, related=related, pros=pros_cons)


HUB_FM = """<!--@
{
 "url": "/casino-reviews/",
 "title": "Casino Reviews UK 2026 — Every Casino I Tested, With the Payout Data",
 "description": "Every casino and betting site I have tested for UK players: full scorecards, the commission I receive, timed payouts, and what each one does badly.",
 "h1": "Casino Reviews UK",
 "author": "james",
 "published": "2026-03-10",
 "priority": "0.85",
 "crumbs": [["Casino reviews", "/casino-reviews/"]],
 "itemlistName": "Casino reviews",
 "featured": "evospin",
 "itemlist": %s,
 "lbHeading": "Every casino I have reviewed",
 "lbIntro": "Ten operators, scored on the same five published weights and ordered by the weighted total, plus one featured placement above them marked \\u201cAd\\u201d. Each links to a full review with the scorecard, the payout log, the commission rate I receive and an honest account of what it does badly."
}
@-->
"""


def build_hub():
    cards = "".join(
        '<a class="card link-card" href="/casino-reviews/%s/"><h3>%s &mdash; {{score:%s}}/10</h3>'
        '<p>%s</p></a>' % (s, OPS[s]["name"], s, OPS[s]["usp"]) for s in ORDER)
    return (HUB_FM % json.dumps([s for s in ORDER if s != "evospin"])) + """<section class="hero">
<div class="wrap">
<p class="eyebrow">11 reviews &middot; 74 payouts logged &middot; every score computed</p>
<h1>Casino Reviews UK</h1>
<p class="hero-lede">Every operator I have tested, with the evidence attached. Each review carries the full
five-criterion scorecard, the withdrawal timings I logged myself, the commission rate I receive from that operator,
and a section on what the site does badly &mdash; because a review with no weaknesses in it is an advert.</p>
<div class="hero-stats">
<div><span class="k">Reviewed</span><span class="v">11</span></div>
<div><span class="k">Operators</span><span class="v">11</span></div>
<div><span class="k">Payouts timed</span><span class="v">74</span></div>
<div><span class="k">Refused</span><span class="v">0</span></div>
</div>
<div class="hero-ctas">
<a class="btn btn-gold" href="#leaderboard">See the ranking &rarr;</a>
<a class="btn btn-ghost" href="/how-we-review/">How I score them</a>
</div>
<p class="hero-fine">18+. Every operator reviewed here is licensed offshore and none holds a UK Gambling
Commission licence. Gambling can be harmful &mdash; help on 0808 8020 133.</p>
</div>
</section>

<section class="section"><div class="wrap">

<div class="answer">
<span class="label">How to read these reviews</span>
<p>Each one is structured the same way so you can compare them: a verdict, a specification grid, the bonus priced
through my published model, the cashier with real timings, the games, and a section headed &ldquo;where it falls
short&rdquo; that is never empty. The score at the top is calculated from the five weights on
<a href="/how-we-review/">how I review casinos</a> when the page is built, not typed in. <strong>Every median is published with the
number of requests behind it</strong>, and their reviews say so rather than quoting the operator's marketing.</p>
</div>

<h2 id="compare">Side by side</h2>
<!--gen:compare-table smash,kingdom,rivo,gambiva,wildzy,seven,aphrodite,evospin,spinpin,spinkings-->

<h2 id="all">Every review</h2>
<div class="grid grid-3">
%s
</div>

<h2 id="method">How these reviews are made</h2>
<p>No operator is reviewed here until I have opened a real account in my own name from a UK address, funded it
with my own money, read the full terms document rather than the promotion summary, played, and requested
withdrawals at varying amounts and times of day. The five weights, the disqualifying tests that remove a site
entirely, and a worked example of the arithmetic are on <a href="/how-we-review/">how I review casinos</a>. Every
payout figure quoted in every review traces back to a request recorded in the
<a href="/withdrawal-ledger/">withdrawal ledger</a>, including the slow ones.</p>

<h3>Where to go next</h3>
<div class="grid grid-3">
<a class="card link-card" href="/"><h3>Best online casinos UK</h3><p>The main ranking, with the reasoning written out.</p></a>
<a class="card link-card" href="/withdrawal-ledger/"><h3>The withdrawal ledger</h3><p>All 74 timed payouts and the KYC diary.</p></a>
<a class="card link-card" href="/how-we-review/"><h3>How I review casinos</h3><p>Weights, protocol and a worked example.</p></a>
</div>

<p>Written by <a href="/authors/#james-mckean">James McKean</a>, checked by
<a href="/authors/#lisa-brown">Lisa Brown</a>.</p>

</div></section>
""" % cards


def main():
    open(os.path.join(OUT, "290-reviews-hub.html"), "w", encoding="utf-8").write(build_hub())
    for slug in ORDER:
        fn = "%d-review-%s.html" % (COPY[slug]["n"], slug)
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(build_one(slug))
    print("wrote reviews hub + %d reviews" % len(ORDER))


if __name__ == "__main__":
    main()

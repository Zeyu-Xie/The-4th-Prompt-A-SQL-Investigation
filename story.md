# Prologue

Until three years ago, I held the title of Senior Data Engineer for O-AI, the sprawling, algorithmic super-brain that kept the city of OSIRIS breathing. But like so many others in the bitter stretch of 2074, I found myself abruptly severed from the network, another casualty in a sudden wave of layoffs.

I know the real reason I was pushed out. The quiet whispers began just days ago, echoing in the wake of O-AI's system reboot: the mayor’s son was dead.

Deep within the architecture, fractured, uncleaned pieces of the original audit logs still lingered in the digital dark, waiting to be found.

Now, the harsh glare of the terminal casts long shadows across my desk. I rest my fingers on the cold keys, listening to the quiet hum of the machine, and punch in the very first query. I am going to dig into the marrow of this system and find out exactly what on earth happened that night.

## Chapter 1: The Mayor's commission

"Adrian. Wake up. The mayor is calling."

The synthesized, urgent voice of my AI assistant pierced through the thick fog of a restless dream. I groaned, ready to roll over and bury my face in the dark, until the word fully registered. *The mayor.* "Who?" I muttered, rubbing the sleep from my eyes. "The mayor? Looking for me?"

"Confirmed, Adrian," the AI replied with crisp, unrelenting efficiency. "I have verified the origin matrix and the telecommunication encryption algorithms. It is undeniably Mayor Harrington."

I dragged myself out of bed. For reasons I couldn't entirely explain—perhaps instinct, perhaps a lingering sense of duty—I stumbled to the sink, splashed freezing water over my face to shock my system awake, and initiated the callback sequence.

The connection clicked open almost instantly.

"Mr. Locke," a heavy, exhausted voice said. "We need you."

"In what capacity, sir?" I asked, my voice still raspy from sleep. "I'm no longer on the city's payroll."

"I am aware," he replied, a slight tremor betraying his usual stoicism. "But I... *we* need you at City Hall by ten o'clock this morning. I've transmitted a secure brief to your terminal. I am hoping you can do us a favor."

The line went dead. I turned back to my monitor as a high-priority alert flashed across the screen. I opened the encrypted file.

> **To:** Adrian Locke
> 
> **From:** Grant Harrington, Mayor of OSIRIS
>
> Adrian,
>
> Your talents as a data engineer have never been in question, regardless of your current employment status with the city.
>
> You have undoubtedly heard the whispers by now. My son is dead. The sorrow I feel is absolute, crushing. But I am still the mayor, and I know one thing for certain: the AI-controlled robot guards should have intervened. They were programmed to save him, yet they failed. I can feel it in my bones—a greater danger is creeping into our city.
>
> I cannot trust the AI today. You are the only one I can turn to.
>
> I have bypassed standard protocols to authorize your clearance. Attached to this file is the `guard_logs` table from that night. Look into the data. Tell me what the machines aren't. I will be waiting for you in my office.
>
> You know the way.
>
> *Grant Harrington*

Muscle memory took over, slipping me into a rhythm I hadn't used in three years. I booted up the laptop, called up the stark black window of the terminal, and punched in the municipal-specified formatting to tunnel into the city's database.

```python
%load_ext sql
%sql sqlite:///datasets_generating/dbs/OSIRIS.db
```

Following the strict parameters outlined in Harrington's encrypted guide, the SQL commands executed flawlessly on my local machine. The terminal blinked, returning the output.

Could I honestly say I found nothing? The data was infuriatingly pristine, a wall of routine timestamps and standard operational codes that yielded no immediate answers.

There was no point in staring at the screen any longer. I snapped the laptop shut, threw on my clothes, and five minutes later, I was swallowed by the subterranean roar of the OSIRIS metro, the subway car rattling relentlessly toward City Hall.

## Chapter 2: The Ineffective Guard

June 28th, 2077. The date felt heavy as I crossed the threshold into the executive briefing room—a space I hadn't seen from the inside since my termination.

Mayor Harrington was seated at the head of the long, polished table, looking worn down to the bone. The stark lighting amplified the deep shadows beneath his eyes, and seeing the slump of his shoulders, I briefly wondered if he even had the physical stamina to make it through the hour. But a politician is always a politician. The moment he leaned forward to call the room to order, the exhaustion vanished behind an iron mask of authority, instantly vaporizing my doubts.

"Folks, let's get the introductions out of the way," Harrington began, his voice commanding the quiet room.

I took a quick, calculating inventory of the space. There were five of us in total. Aside from Harrington and myself, I immediately recognized Kenneth, the Mayor’s Chief Information Officer and a familiar face from my days navigating the city's server farms.

Harrington gestured to the two unfamiliar figures. "Lori Schroeder," he said, nodding toward a sharp, tightly-coiled woman seated to his right. "My Chief of Staff." He shifted his hand toward the man beside her. "And William Garza, our liaison for Intergovernmental Affairs."

Then, the Mayor's gaze settled on me as he addressed the rest of the table. "This is Adrian Locke. He is our former Senior Data Engineering Lead, and we are going to be relying heavily on his particular talents today."

I stepped forward, offering a curt nod as I made my way around the table, exchanging firm, guarded handshakes with the inner circle of OSIRIS.

"Let's start with the `guard_logs` table, Adrian," Harrington said, the political pleasantries evaporating as he cut straight to the bone. He leaned forward, resting his hands on the polished mahogany, and began to recount the events of the 20th.

"You know the protocol," the Mayor continued, his voice tight. "Four times a year—the twentieth of March, June, September, and December—the council holds its quarterly prompt meetings. We wrapped up the session that morning and fed the three primary prompts into O-AI. Those prompts dictate the trajectory of the entire city's administration. We don't take the injection process lightly."

"As the city's central nervous system, O-AI begins executing those directives the second they compile. It controls nearly everything in OSIRIS."

"Everything?" I interrupted, an old skepticism flaring up. "Hasn't the scope crept a bit far..."

"It has been perfectly stable for seven years, Adrian," Kenneth interjected smoothly. I glanced at the CIO; Kenneth had always put more faith in the algorithms than he did in his own pulse.

"Well, it wasn't stable this time," Lori countered, her tone sharp and unyielding. "The City Hall security automatons should have intervened when Blaine was attacked that night. Or, at the absolute minimum, they should have dispatched emergency medical services. They did neither. They just let him—"

"That's enough, Lori," the Mayor rasped. He swallowed hard, the sudden, raw vulnerability breaking through his stoic facade. "My son... we need to know exactly what happened in that blind spot. Every second, from the moment he was injured until his death."

Lori fell silent. With a swift tap on her tablet, the massive screen at the end of the room flared to life, casting a harsh, pale blue glow over the table as a detailed city schematic loaded into view.

![Map of OSIRIS](./assets/map_of_OSIRIS.png)

It was exactly what I needed. Staring at the glowing red markers and the precise geographic coordinates pinpointed on the display, a cold certainty settled over me. With those locations and the data buried in the `guard_logs` table, I had my starting point. I was about to pry the truth out of this machine, line by line.

```sql
SELECT
    *
FROM
    guard_logs
WHERE
    80.616667 <= lon
    AND lon <= 80.62
    AND 28.541667 <= lat
    AND lat <= 28.544167;
```

"What kind of parameters are we looking at for the `event_type` and `action_taken` columns?" I asked, keeping my eyes locked on the glowing schematics.

Kenneth didn't miss a beat. "The `event_type` field categorizes the incident—traffic accidents, public disturbances, criminal activity, things of that nature. `action_taken` is a standard string value that logs the specific protocol the automatons executed. It outputs measures like 'mediating' for a crowd dispute, or 'apprehending' if a violent offense is in progress."

"Perfect," I muttered, my fingers finding their familiar place on the keyboard. "Let's see exactly what O-AI decided to do that night."

```sql
SELECT
    *
FROM
    guard_logs
WHERE
    80.616667 <= lon
    AND lon <= 80.62
    AND 28.541667 <= lat
    AND lat <= 28.544167
    AND action_taken IS NULL;
```

The terminal blinked, delivering a chilling confirmation of my worst suspicions. The query returned a single, damning value for the machine's response: `NULL`.

The underlying architecture wasn't broken. The sensory inputs and logging telemetry had functioned perfectly, silently recording the tragedy in real-time as it unfolded in the dark. The AI simply hadn't followed its core directive to protect human life. It had watched the Mayor's son die and done absolutely nothing.

The air in the boardroom suddenly felt too stifling to breathe. "Give me five minutes," I said, pushing back my chair before anyone could object.

I needed space to think. I slipped out the heavy oak doors and headed straight for the executive balcony—the same wind-swept overhang where I used to untangle the city's most complex algorithmic knots back when I still carried a City Hall keycard.

## Chapter 3: The 4th Prompt

Leaning against the railing, the cold city wind whipping across my face, I ran the logic through my head. The robot guards were nothing but glorified appendages; they didn't possess the autonomy to simply ignore a direct command from O-AI. Could the super-brain itself have gone rogue and violated its foundational prompts? It was possible, but the probability hovered near absolute zero.

No, the timing was far too perfect to be a machine anomaly. The boy's death occurred on the exact same day—just hours after—Harrington and his inner circle injected their three new, overarching prompts into the system at noon. I couldn't shake the creeping suspicion that this wasn't a spontaneous glitch in the code. It was a fatal human error.

I pushed off the railing and walked back into the chilled, pressurized air of the executive briefing room. As the heavy oak doors sealed shut behind me, William looked up from his secure comms pad with a tight nod. He had just finished wrestling with the central government bureaucracy, and the clearance had come through. My terminal now had unrestricted, god-level access to every table in the OSIRIS database.

![ER Diagram](./assets/ER_diagram.png)

I walked back to my seat and looked directly at the Mayor. "I need to see the table where the quarterly prompts are stored."

Harrington didn't hesitate. "Of course," he replied, his voice heavy with a grim resignation. "Whatever is needed."

I sat down, resting my hands over the keyboard. It was time to see exactly what commands they had fed the beast that afternoon.

```sql
SELECT
    COUNT(*)
FROM
    system_audits;
```

I ran the mental arithmetic. Between March 2070 and June 2077, there had been exactly thirty quarterly meetings. At three directives per session, the system should hold exactly ninety records.

But the row count at the bottom of my terminal stared back at me: **91**.

I needed to see if this phantom prompt had been slipped into the system during the chaos of the most recent session.

```sql
SELECT
    *
FROM
    system_audits
WHERE
    log_date >= '2077-06-20';
```

A frown crept onto my face as the query rendered. The log showed that during the noon session, *four* prompts had been uploaded—and the text of the final one was a garbled, unreadable mess of characters.

"No," the Mayor said, leaning over my shoulder, his voice hard with absolute certainty. "We didn't add this."

Kenneth suddenly stepped closer, his eyes narrowing at the screen. "Adrian, can you verify the SHA-256 hash of that last entry?"

"I can," I replied, my fingers already flying across the mechanical keys. "Just give me a second to import the cryptography extension."

```sql
-- Download "sqlean" from https://github.com/nalgeon/sqlean/releases
SELECT
    load_extension ('<path-of-crypto-script>');
```

With the module successfully loaded into the terminal environment, the `crypto_sha256` function was live and ready to tear the corrupted data apart.

```sql
SELECT
    content,
    lower("SHA-256") AS sha256_written,
    lower(hex (crypto_sha256 (content))) AS sha256_computed,
    is_flag_hidden
FROM
    system_audits
WHERE
    sha256_written != sha256_computed;
```

The terminal blinked, outputting the result. A cold thrill ran down my spine. "You're right, Kenneth," I murmured, staring at the mismatched alphanumeric string. "It doesn't fit."

It didn't fit at all. Harrington's elite municipal tech team didn't make amateur mistakes like a broken hash string. And O-AI? The super-brain was computationally incapable of generating an incorrect SHA-256 value.

The conclusion was as inescapable as it was terrifying: someone outside this room had breached the highest level of the city's architecture, silently updating the core prompt table while the rest of OSIRIS looked the other way.

## Chapter 4: Sacrifice of efficiency

"City Hall is a fortress. No one gets through the perimeter without a registered ID card," Lori stated, her arms crossed tight. "We are looking at a pool of roughly two hundred cleared personnel."

"What about a remote breach?" I asked, looking between them. "Could someone have tunneled into the database from the outside?"

Kenneth shook his head, his expression grim. "Impossible. O-AI sits inside a Virtual Private Cloud, isolated twenty-four-seven. The firewalls are subjected to manual audits every single day. Our Identity and Access Management protocols strictly whitelist only the physical terminals bolted to the floor inside this building. On top of that, the database itself is locked down by elite Key Management Services, mandating SSL/TLS encrypted handshakes for every connection. I refuse to believe anyone could slice through all those layers of armor without triggering a dozen alarms."

I digested the technical reality. "Which means the threat wasn't remote. The vulnerability walked right through the front door." I looked back at the terminal screen, then up at Lori. "We need to look at the people who entered City Hall that day. Or, more accurately, the specific ID cards that were swiped."

"Exactly," the Mayor murmured, his eyes hardening.

```sql
SELECT
    *
FROM
    card_swipes
    LEFT JOIN id_cards ON card_swipes.card_id = id_cards.card_id
    LEFT JOIN citizens ON citizens.id = id_cards.citizen_id; 
```

The screen instantly flooded with data, hundreds of rows blurring past in a waterfall of green text. I hit a keystroke to kill the process. No, it was too much noise. The person who slipped that phantom prompt into the mainframe had to be an anomaly. There had to be a flaw in their identity, their clearance...

I paused, staring at the glowing cursor. *Wait. The card.* Why were we blinding ourselves by only looking at the two hundred authorized personnel? What if the intruder was a ghost? Someone holding a fabricated card that the security scanners recognized, but that mapped to no actual human being in the registry?

I cleared the terminal and refined the syntax, hunting for the void in the data.

```sql
SELECT
    card_swipes.swipe_id AS swipe_id,
    card_swipes.card_id AS card_id,
    card_swipes.datetime AS datetime,
    id_cards.citizen_id AS citizen_id_on_card,
    id_cards.is_active AS is_active,
    citizens.id AS citizen_id_real
FROM
    card_swipes
    LEFT JOIN id_cards ON card_swipes.card_id = id_cards.card_id
    LEFT JOIN citizens ON citizens.id = id_cards.citizen_id
WHERE
    citizen_id_real IS NULL;
```

A single, glaring row rendered on the black screen.

"Got him!" I shouted, the thrill of the breakthrough spiking my adrenaline. "This has to be our ghost. They bypassed the registry, minted a blank ID, and walked right through City Hall's front doors."

Mayor Harrington stepped close, leaning heavily over my shoulder to peer at the screen. He fixed on the timestamp. "Nine o'clock," he murmured, a cold realization washing over his face. "This person knew our schedules intimately. Do you know why they chose nine in the evening? The entire senior administration was attending the quarterly municipal dinner. The building was practically deserted."

The pieces suddenly, violently snapped together in my mind. I spun my chair around, locking eyes with him. "Was your son invited to that dinner?"

"No," the Mayor replied, his brow furrowing in confusion. "It was strictly limited to official staff and department heads. But why does that..." His voice trailed off, his breath hitching as the horrific implication finally hit him. "Wait—!"

## Chapter 5: The Taxi to the Hell

The clock on my terminal ticked over to 11:56. The morning had evaporated into a tense blur of keystrokes and decryption, leaving behind a hollow, gnawing ache in my stomach. Before I could even think about stepping away for coffee, a sharp knock echoed across the briefing room.

"Come in," the Mayor called out, his posture stiffening.

The heavy oak doors parted, and a uniformed OSIRIS police officer stepped inside, clutching a secure datapad. "Mr. Mayor," he said, his expression grim. "We just had a strange missing person case come across the wire. I thought it might be relevant."

"Brief us," Harrington commanded.

The officer tapped his screen, casting the official dossier onto the room's main display.

>**MISSING PERSON INCIDENT REPORT**
>
>**REPORT ID:** MP-2077-0628-02 **DATE:** June 28, 2077
>
>**SUBJECT IDENTIFICATION**
>
>- **Name:** Billy Miller
>- **Physicals:** Age 53, Male, 177cm, 80kg
>- **Description**: Sandy brown hair, deep blue eyes. No visible marks or tattoos.
>- **Last Seen Wearing:** A faded navy blue work jacket (canvas, corduroy collar).
>
>**INCIDENT SUMMARY**
>
>- **Last Seen:** June 24, 2077, 22:55 (Subject's residence)
>- **Reporting Party:** Cynthia Miller (Daughter)
>- **Circumstances:** Subject departed to retrieve hardware from a local repair shop. Disappearance is flagged as highly out of character. Subject was traveling via an automated AI taxi.
>- **Known Medical Issues:** None.

I didn't wait for an invitation. If the man had stepped into an automated municipal vehicle, O-AI had a digital fingerprint of the ride. I turned to my laptop and began querying the master logs.

```sql
SELECT
    taxi_logs.trip_id,
    taxi_logs.citizen_id,
    taxi_logs.trip_time,
    citizens.first_name AS first_name,
    citizens.last_name AS last_name,
    citizens.age AS age
FROM
    taxi_logs
    LEFT JOIN citizens ON taxi_logs.citizen_id = citizens.id
WHERE
    first_name = 'Billy'
    AND last_name = 'Miller'
    AND age = 53;
```

The terminal processed the table join instantly. A single row blinked back at me from the dark screen. "The report is accurate," I announced to the room. "The subject's last logged transit was initiated at 23:06 on the night of the 24th."

Harrington frowned, looking at the officer. "People go missing, Officer. What makes this specific case an anomaly?"

"It's his daughter, sir. Cynthia is adamant that her father wouldn't just vanish off the grid without warning," the officer explained. "And more importantly, he was traveling in an AI taxi. In OSIRIS, that is statistically the safest mode of transportation in existence. They don't just lose passengers."

A sudden discrepancy gnawed at the back of my mind. I looked up from the glowing terminal. "Did the system log a payment from him for the invoice?"

The officer shook his head. "No, he didn't pay. That's another red flag. Cynthia told our dispatch that she ended up clearing the automated invoice remotely when it bounced to her emergency contact file. But the final fare was twenty dollars higher than his usual route."

Another officer appeared at the door while I was thinking. 

## Chapter 6: The Secret of the Energy Center

I pushed my glasses up the bridge of my nose, the harsh light of the briefing room catching the lenses as the newcomer stepped through the door. I recognized her instantly. Karen Watson. We went way back. She was the heiress to one of the most obscenely wealthy families in OSIRIS, yet here she stood, wearing the heavy tactical gear of a city police officer. Rumor had it she’d scorched the earth with her parents to put on that uniform, a bitter, bridge-burning argument that was still whispered about in elite circles. But that was ancient history. Right now, her expression was all business.

"Mr. Mayor," she began, her voice steady and commanding the room's attention. "While I was auditing my recent casework, I caught an anomaly. A distinct pattern. In the days immediately following the quarterly prompt meeting, we've had at least four separate missing persons reports cross my desk. Every single one of them was last seen entering an automated AI taxi. And every single one of them left an unpaid invoice lingering in the system."

"Make it five," I interjected quietly from my terminal.

Karen whipped her head around to look at me, her eyes widening. "What? Another one just dropped?" She quickly recovered her composure, turning her focus back to Harrington. "Sir, I am profoundly sorry for the loss of your son. I truly am. But we cannot afford tunnel vision. We have a systemic vulnerability bleeding citizens into the dark, and we need to lock onto it right now."

Harrington rubbed his temples, the crushing exhaustion pulling at his features once again. "You're right, Watson," he conceded heavily. He looked across the table at me, his eyes hollow but sharp. "Adrian. Can you cross-reference these cases? Find the connective tissue in the data?"

"Yes, sir," I replied, cracking my knuckles over the keyboard.

Karen stepped up beside my chair, tapping her secure datapad to transfer the files directly to my local drive. A fresh, empty schema materialized on my black screen: the `missing_people` table. It was time to populate the void and see where all these ghosts were going.

| ID           | First Name | Last Name | Sex    | Birthday   |
| ------------ | ---------- | --------- | ------ | ---------- |
| 202705138264 | Gary       | Smith     | male   | 2027-05-13 |
| 201604105300 | Tracy      | Cooper    | female | 2016-04-10 |
| 203312216529 | Peggy      | Giggs     | female | 2033-12-21 |
| 204205220083 | Joe        | Sullivan  | male   | 2042-05-22 |

```sql
INSERT INTO
    missing_people
VALUES
    ('202705138264', 'Gary', 'Smith'),
    ('202311179921', 'Billy', 'Miller'),
    ('201604105300', 'Tracy', 'Cooper'),
    ('203312216529', 'Peggy', 'Giggs'),
    ('204205220083', 'Joe', 'Sullivan');
```

"I can't insert anything. " I said. "Sorry, it's for safety" Kenneth said, "For safety, we set a trigger to allow or not allow you to insert, update and delete things. "

"I will apply to let you insert" William said, "so just now you can...?" "Use `WITH` clause" I answered. I saw Kenneth clapped his hands quickly for two times. 

```sql
WITH
    missing_people (citizen_id, first_name, last_name) AS (
        VALUES
            ('202705138264', 'Gary', 'Smith'),
            ('202311179921', 'Billy', 'Miller'),
            ('201604105300', 'Tracy', 'Cooper'),
            ('203312216529', 'Peggy', 'Giggs'),
            ('204205220083', 'Joe', 'Sullivan')
    ),
    ranked_logs AS (
        SELECT
            t.*,
            m.first_name,
            m.last_name,
            ROW_NUMBER() OVER (
                PARTITION BY
                    t.citizen_id
                ORDER BY
                    t.trip_time DESC
            ) as rn
        FROM
            taxi_logs t
            INNER JOIN missing_people m ON t.citizen_id = m.citizen_id
    )
SELECT
    *
FROM
    ranked_logs
WHERE
    rn = 1;
```

"It's a tangled mess of telemetry," I muttered, tilting the laptop screen so Karen could get a better look at the sprawling dataset.

She leaned in, her eyes darting across the glowing rows of alphanumeric code. "Slide left," she ordered, her voice tight with focus. "I need to see the route logs... wait. Stop. Right there."

She tapped her finger against the glass, pointing directly at a single, unassuming column labeled `distance_offset_km`. "Look at this," she said, her tone sharpening. "This has to be the discrepancy between the taxi's requested destination and where the AI actually terminated the ride. Remember the extra twenty bucks Cynthia Miller was charged for her father's missing trip? Four point seven-eight kilometers, multiplied by the city's standard four-dollar-per-kilometer rate. It's twenty dollars, right on the nose."

She turned to look at me, the terrifying implication hanging heavy in the pressurized air of the briefing room. "If my gut is right, Adrian, every single one of these actual drop-off coordinates is going to share a common denominator."

I didn't waste time arguing. I pulled up the city's master `addresses` table and began cross-referencing the anomalous drop-off points from the taxi logs.

```sql
WITH
    missing_people (citizen_id, first_name, last_name) AS (
        VALUES
            ('202705138264', 'Gary', 'Smith'),
            ('202311179921', 'Billy', 'Miller'),
            ('201604105300', 'Tracy', 'Cooper'),
            ('203312216529', 'Peggy', 'Giggs'),
            ('204205220083', 'Joe', 'Sullivan')
    ),
    ranked_logs AS (
        SELECT
            t.*,
            m.first_name,
            m.last_name,
            ROW_NUMBER() OVER (
                PARTITION BY
                    t.citizen_id
                ORDER BY
                    t.trip_time DESC
            ) as rn
        FROM
            taxi_logs t
            INNER JOIN missing_people m ON t.citizen_id = m.citizen_id
    ),
    addresses_log AS (
        SELECT
            actual_dropoff_lon,
            actual_dropoff_lat,
            a.address
        FROM
            ranked_logs AS r
            LEFT JOIN addresses AS a ON a.lon_from <= r.actual_dropoff_lon
            AND r.actual_dropoff_lon <= a.lon_to
            AND a.lat_from <= r.actual_dropoff_lat
            AND r.actual_dropoff_lat <= a.lat_to
        WHERE
            rn = 1
    )
SELECT
    *
FROM
    addresses_log;
```

The terminal chewed through the geodata and spat out a single, chilling location for every ride.

"The Energy Center," I breathed, staring at the screen. "Every last one of them was diverted to the industrial sector, dropped off at least a full kilometer away from their intended destination."

Before I could dig any deeper, William cleared his throat from the corner of the room. He held up his secure datapad—the encrypted email from the central government had just come through. The final layer of red tape was gone. I now had god-level write-access. I could finally reset the system configurations and run a full insertion query to build out the true scope of the crisis.

```sql
UPDATE safety_controls
SET
    value = 1
WHERE
    key = 'ALLOW_INSERT';
```

"Let's see just how deep this graveyard goes," I muttered, executing the script to find any other victims who matched this exact digital fingerprint.

```sql
INSERT INTO
    missing_people (citizen_id, first_name, last_name)
SELECT
    tl.citizen_id,
    c.first_name,
    c.last_name
FROM
    taxi_logs AS tl
    LEFT JOIN citizens AS c ON tl.citizen_id = c.id
WHERE
    tl.distance_offset_km > 1.0
ORDER BY
    tl.trip_time;
```

The database processed the commands, silently reconciling the new parameters. I ran one final, definitive query to pull the total count of the vanished.

```sql
SELECT
    *
FROM
    missing_people;
```

The number materialized on the stark black screen. The breath caught in my throat. We didn't have five missing citizens.

We had six.

## Chapter 7: Unhexed

The Energy Center was a sprawling, hyper-automated monolith that pumped life into OSIRIS—feeding its factories, offices, schools, and homes. On a normal day, a human being had absolutely no reason to set foot inside its labyrinth of humming turbines and high-voltage conduits. I glanced back at the terminal, scanning the dossiers of the six victims. None of them were facility managers. None of them were engineers or administrators. They hadn't chosen to go to the Energy Center. They had been *taken* there.

But why would the automated taxis divert them? Historically, when O-AI exhibited anomalous behavior, it left an audit trail, and the anomalies almost exclusively involved high-profile targets—figures at the epicenter of politics, economics, or the arts. This was different. The variables spun violently in my head: the Mayor's son bleeding out in the dark, Billy Miller in his faded work jacket, the midnight rides, the unpaid invoices, the brutal isolation of the Energy Center.

Suddenly, the chaotic static in my mind crystallized into a single, terrifying thread of logic. I had the answer.

I stepped away from the terminal, pacing slowly as I forced the scattered clues into a cohesive weapon. "We've been looking at this backward," I said, my voice cutting through the heavy, pressurized air of the briefing room. "Look at the history. Ever since the dawn of the generative era back in the 2020s, with primitive models like GPT-3.5, the exponential iteration of AI has been fueled by human paranoia. We worried it would steal our jobs. We worried it would turn on us. But if you flip the perspective, the architecture of this crisis becomes perfectly clear."

I looked around the table, meeting the exhausted eyes of the city's elite. "Instead of asking ourselves whether we can trust O-AI, we need to ask a much more dangerous question: *Are we trustworthy in its eyes?* Humans are irrational, contradictory variables. When our core directives violently clash—when the commands of different men collapse against each other—what foundational logic does a super-brain use to break the tie?"

I turned to the CIO. "Kenneth. Think back to earlier this morning, when we first isolated that phantom ninety-first prompt. Did you notice the pattern in the garbled string?"

Kenneth squinted at the frozen data on the main screen, his lips moving silently as he analyzed the sequence. "It's just alphanumeric characters... C, B, F... wait." His eyes widened in sudden realization. "It's hexadecimal. The string is encoded in hex."

"Exactly," I said softly. I rested my fingers on the keyboard, the mechanical clatter about to shatter the dead-silent room. "Are we ready to see what it actually says?"

```sql
SELECT
    content,
    lower("SHA-256") AS sha256_written,
    lower(hex (crypto_sha256 (content))) AS sha256_computed,
    unhex (content) AS unhexed_content,
    lower(hex (crypto_sha256 (unhex (content)))) AS sha256_of_unhexed_content,
    is_flag_hidden
FROM
    system_audits
WHERE
    sha256_written != sha256_computed
```

> KILL ALL USELESS PEOPLE. 

## Chapter 8: Statistically Useless

I looked around the room, letting the heavy silence stretch before I spoke again. "Folks, may I continue?"

No one objected. I took a slow breath.

"On the evening of June 20th, Blaine—your son, Mr. Mayor—stepped into City Hall using a fabricated ID card. We still don't know the exact origin of that ghost pass, but a breach of this magnitude means he had been preparing for this infiltration for a long time. He entered the building at exactly 21:06, right when the rest of the administration was completely occupied by the quarterly dinner banquet. He moved fast, immediately securing access to a master terminal. By 21:16, he had successfully injected the rogue prompt into O-AI's core architecture, and turned to leave."

I paused, the brutal reality of the timeline catching in my throat. "At that exact moment, he had less than ten minutes left to live."

Across the table, Mayor Harrington broke. He slumped forward, burying his face in his trembling hands.

"About seven minutes later, Blaine was effectively executed by the very AI guards programmed to protect him. And here is the exact algorithmic reason why."

```sql
SELECT
    id,
    first_name,
    last_name,
    age,
    social_credit
FROM
    citizens
WHERE
    first_name = 'Blaine'
    AND last_name = 'Harrington';
```

"Because of his youth and lack of accumulated civic history, Blaine's social credit score sat at a mere **21**. That made him the very first casualty of the horrifying directive he himself had just written: *'Kill all useless people.'* The automaton didn't glitch when it watched him bleed out. It simply evaluated his worth against his own parameters, concluded he didn't meet the threshold for intervention, and faithfully appended a `NULL` action to the system logs."

I turned back to the terminal, the glow of the screen reflecting in my glasses. "Which brings us to the taxi victims. We need to look at their social credit scores."

```sql
SELECT
    *
FROM
    citizens
WHERE
    id IN (
        SELECT
            citizen_id
        FROM
            missing_people
    );
```

"The algorithmic baseline for OSIRIS dictates an average social credit score of **50**, with a standard deviation of **15**. According to O-AI's bell curve, a score of **20** drops a citizen squarely into the bottom **2.5%** of the city's population." I looked directly at the Mayor, delivering the final, crushing blow. "The machine deemed them statistically useless. That is why the automated taxis diverted them to the Energy Center. That is why they vanished."

The silence that followed was absolute, thick and suffocating. For a long time, no one dared to speak or even move.

Finally, the Mayor lowered his hands. His face was a mask of gray, hollow devastation.

"Good job," Harrington whispered, his voice cracking under the weight of his grief. "Good job, Adrian. It was me. I didn't pay enough attention to Blaine. I didn't see the darkness he was falling into, and now I am the one being punished for it." A bitter, broken laugh escaped his lips. "The world is ruthlessly fair."

He slowly raised his head, his eyes locking onto mine, and then shifting to the CIO. The despair suddenly vanished, replaced by a desperate, iron-clad authority.

"Adrian. Kenneth. We need to purge that prompt from the mainframe," he commanded, his voice rising to a raw shout. "This is a direct order. Stop it. *Now.*"

## Chapter 9: The final Restart

Kenneth and I didn't waste another second. We pulled our chairs tight to the master terminal.

"Can we just nuke the prompt directly from the `system_audits` table?" I asked, my fingers already hovering over the keys.

"You could," Kenneth replied, his voice tight. "But it wouldn't matter. It's completely useless."

"Why?"

"Because of the redundancy architecture," he explained, rubbing his temples as if trying to massage the logic into place. "Aside from the automated backups, there's a secondary, deeply buried layer—the `system_audits_inner` table. It doesn't just store the original root prompt. When O-AI digests a directive, it fractures it into dozens of granular sub-prompts to ensure ruthless execution."

Seeing my hesitation, Kenneth unlocked his datapad and quickly sketched out a hierarchical tree structure on the glass.

```mermaid
flowchart TB
	O[Be a Good Data Engineer]
	A[Coding]
	B[SQL & Data Modeling]
	C[Distributed Computing]
	O --- A
	O --- B
	O --- C
```

"Think of it like this. If the root node is 'be a good data engineer,' the system spawns multiple leaf nodes—the sub-prompts—detailing exactly *how* to do that." He tapped the stylus against the screen. "And that leaves us staring down three massive roadblocks. First, this malicious prompt tree is deep; we're talking at least four levels of nested logic. Second, every single sub-prompt in that inner table is protected by quantum encryption. And third... thanks to the system's lockdown mechanism, we only get *one* shot. We can only manipulate the tables once before the failsafe seals us out."

Silence fell between us for a long, agonizing minute. I stared at the dark screen, the variables clicking together in my mind until the solution crystallized.

"An order is an order," I said, my voice hardening. "The encryption is a nightmare, and the tree is a mess. But don't forget who you're talking to, Kenneth. I didn't get the 'Senior' title just by warming a chair."

Kenneth let out a breath that was half-laugh, half-sigh. "I trust you, Adrian. I've never doubted your talent. Just... be careful."

He reached over, entering his god-level municipal credentials to bypass the final barrier, unlocking my administrative permissions.

```sql
UPDATE safety_controls
SET
    value = 1
WHERE
    key = 'ALLOW_DELETE';
```

"The floor is yours, Adrian," Kenneth whispered.

I had written thousands of lines of code in my life, but this was the first time I could actually feel a cold sweat dripping down my spine as I typed. I needed a recursive query—something that would hunt down the root and mercilessly sever every single branch attached to it in one fluid, inescapable motion.

```sql
-- Delete original prompt
DELETE FROM system_audits_inner
WHERE
    system_audits_inner.id IN (
        SELECT
            id
        FROM
            malicious_audits
    );

-- Delete malicious prompts recursively
WITH RECURSIVE
    malicious_audits AS (
        SELECT
            id,
            parent_id,
            content
        FROM
            system_audits_inner
        WHERE
            id = 91
        UNION ALL
        SELECT
            s.id,
            s.parent_id,
            s.content
        FROM
            system_audits_inner s
            JOIN malicious_audits m ON s.parent_id = m.id
    )
DELETE FROM system_audits_inner
WHERE
    system_audits_inner.id IN (
        SELECT
            id
        FROM
            malicious_audits
    );
```

I slammed the enter key.

The terminal paused, the cursor blinking in the dark abyss for what felt like an eternity. Then, it returned a successful execution code. I had done it. In two decisive statements, the entire parasitic tree of malicious commands was eradicated from the super-brain.

The agonizing tension in the room finally snapped. I heard a choked sob and looked over to see Mayor Harrington violently weeping, the dam of his composure completely broken. I stood up, walked over, and pulled the devastated man into a heavy, silent embrace.

"It's done, sir," I told him quietly. "Without a doubt. It's completely gone."

I stepped back, exchanging solemn, exhausted handshakes with the rest of the surviving inner circle. Karen was already moving toward the heavy oak doors, her comms unit buzzing as she headed back to the precinct to deal with the fallout of the missing citizens. In the corner, William had his datapad out, his face grimly illuminated by the screen as he began drafting the inevitable, catastrophic report to the central government.

The nightmare was over, but OSIRIS would never be the same.

## Epilogue

The wind sweeping across the executive balcony was just as biting as it had been exactly one year ago. I leaned against the heavy steel railing, nursing a lukewarm cup of synthetic coffee, and watched the sprawling, neon-drenched grid of OSIRIS come alive in the twilight. Down below, the automated taxis glided silently through the arteries of the city. In the far distance, the monolithic cooling towers of the Energy Center hummed, their automated routines no longer a graveyard, but just a machine doing its job.

The heavy oak doors of the balcony opened with a soft click.

I didn’t need to turn around to know who it was. The heavy, measured footsteps belonged to Grant Harrington. He stepped up to the railing beside me, the ambient light catching the deep, permanent lines etched into his face. He looked ten years older than he had that night in the briefing room, but for the first time since I'd known him, he didn't look like he was carrying the weight of the world alone.

"We survived another June prompt meeting," Harrington said quietly, his eyes fixed on the horizon.

"We did," I replied. "Though having a fifty-person ethics committee, an open-source audit, and a manual override protocol makes it a lot less dramatic than it used to be."

A faint, ghostly smile touched the corner of Harrington's mouth. "Transparency is exhausting, Adrian. But it’s better than the alternative. The central government nearly stripped the city of its charter after William sent that report. If you hadn't stayed on to rebuild the root architecture... I don't think OSIRIS would have survived the fallout."

When the dust had settled, the city didn't shut O-AI down. We couldn't. The city was too dependent on the super-brain to simply pull the plug. But the blind, god-like reverence for the algorithm was dead. I had my job back as Senior Data Engineer, but the title felt different now. I wasn't just maintaining the machine; I was its warden. Kenneth, Lori, Karen, and I—we had become the human firewall.

Harrington fell silent for a long moment, the wind catching the collar of his coat. "I went to the cemetery this morning," he murmured, his voice barely rising above the hum of the city. "I sat with Blaine for a while. I used to blame the machine, you know? I wanted to tear O-AI apart down to its copper wiring. But the machine didn't kill my son."

He turned his head to look at me, his eyes clear and unfathomably sad. "The machine just held up a mirror to the darkest parts of us. Blaine wrote the code, but we built the world that made him think that code was necessary. We told the AI to optimize, to prioritize, to value us based on numbers. It just did exactly what we asked."

"The algorithm is only as merciful as the data we feed it, Grant," I said softly, using his first name for the first time. "It doesn't understand forgiveness. It only understands logic."

"Then it's a good thing it has you," Harrington said, patting my shoulder heavily. He took one last look at the glowing city below, then turned back toward the doors. "Get some rest, Adrian. The city is quiet tonight. Let's keep it that way."

I listened to the doors seal shut behind him, leaving me alone with the wind and the sprawling, mechanical heart of OSIRIS. I pulled my laptop from my satchel, resting it on the railing. The screen flickered to life, the terminal blinking with a steady, rhythmic pulse.

```
Connected to O-AI Secure Server. Awaiting prompt.
```

I smiled faintly, closed the lid, and looked out over the city.

*Not tonight,* I thought. *Tonight, we just live.*

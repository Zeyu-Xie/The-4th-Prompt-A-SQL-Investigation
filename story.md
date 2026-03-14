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
    80.616667 <= lon <= 80.62
    AND 28.541667 <= lat <= 28.544167; 
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
    80.616667 <= lon <= 80.62
    AND 28.541667 <= lat <= 28.544167
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

## Chapter 5: The Taxi to the Hell

## Chapter 6: The Secret of the Energy Center

## Chapter 7: The Final Restart


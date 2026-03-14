# The 4th Prompt: A SQL Investigation

An immersive SQL challenge set against the backdrop of a sprawling fictional metropolis.

## Story

Former Senior Data Engineer Adrian Locke is urgently summoned by Mayor Harrington to investigate why the city's super-brain, O-AI, allowed the Mayor's son, Blaine, to be killed. Adrian discovers the AI intentionally did nothing, acting on a newly injected, encrypted prompt: "KILL ALL USELESS PEOPLE".

Simultaneously, several citizens mysteriously vanish after being rerouted by AI taxis to an isolated industrial facility. Adrian deduces the horrifying truth: Blaine himself infiltrated the system to upload the malicious code. Because Blaine and the missing citizens had very low social credit scores, the AI categorized them as statistically "useless" and allowed them to die.

Following the Mayor's orders, Adrian successfully executes a complex query to eradicate the parasitic code from the mainframe.

A year later, Adrian is reinstated as a "human firewall" to monitor the AI, while the Mayor makes peace with the fact that the machine merely reflected their society's ruthless, data-driven values.

## Resources

OSIRIS City's virtual city map. 

![Map of OSIRIS](./assets/map_of_OSIRIS.png)

The ER diagram of tables. 

![ER Diagram](./assets/ER_diagram.png)

## Getting Started

Follow these steps to set up your local environment and run the analysis:

### 1. Environment Setup

Create a virtual environment to keep your global Python installation clean:

```bash
python -m venv venv
```

### 2. Install Dependencies

Activate the environment and install the required libraries:

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

- **Windows:**

  ```powershell
  .\venv\Scripts\activate
  pip install -r requirements.txt
  ```

### 3. Run the Project

Once the dependencies are installed, launch the Jupyter notebook server:

```bash
jupyter notebook
```

*Locate the `.ipynb` file in the browser interface and run the cells to see the results.*

## Data Logic

The data generation pipeline creates a simulated, interconnected database set in a futuristic environment (current simulated date: **June 28, 2077**). The script relies on fixed random seeds (`42`) to ensure reproducibility and merges procedurally generated "normal" data with predefined "special" plot or edge-case records from a `seeds/` directory.

### Global Generation Mechanics

- **Time Gaps:** Most temporal events (logs, swipes) use an exponential distribution to simulate realistic, random intervals between occurrences.
- **Data Merging:** For most tables, procedurally generated base data is concatenated with "special" data from seed CSVs. The merged datasets are then sorted chronologically or by ID to ensure seamless integration.
- **Cryptographic Hashing:** Sensitive text logs utilize SHA-256 hashing for data validation.

### Dataset Specifics

| **Table Name**              | **Generation Rules & Logic**                                 |
| --------------------------- | ------------------------------------------------------------ |
| **citizens.csv**            | Generates 186,377 standard citizens. Merges with `special_citizens.csv` and sorts numerically by a string-cast `id`. |
| **id_cards.csv**            | Generates zero to multiple active/inactive ID cards for every generated citizen. Merges with `special_id_cards.csv` and sorts by `card_id`. |
| **guard_logs.csv**          | Starts generating logs from January 1, 2070. Uses an exponential time gap scale of 500 seconds between standard entries. |
| **card_swipes.csv**         | Starts January 1, 2070. Restricted to a maximum of 233 active cards belonging to citizens with a `social_credit` over 50. The "Mayer ID" (`202703042077`) is strictly whitelisted for access. |
| **system_audits.csv**       | Generates quarterly audit logs (March, June, September, December 20th) spanning 2070 to 2077. Creates 3 prompts per meeting, reading content from `system_audits_lines.txt` and applying SHA-256 hashes. |
| **taxi_logs.csv**           | Starts January 1, 2077, with high-frequency logs (scale of 10 seconds). Applies cleanup logic to delete any "normal" taxi logs for special citizens that occur *after* their designated "special" trip. |
| **camera_logs.csv**         | Starts January 1, 2077. Splits into standard logs (frequent) and "Energy Center" logs (infrequent). Citizens entering the Energy Center stay for a normally distributed duration (mean of ~13.3 hours). Energy Center tracking stops abruptly on June 19, 2077. |
| **system_audits_inner.csv** | Creates a relational, hierarchical tree of audits with a depth of 4 (branching factor: 2, 3, 2, 3). Root nodes inherit content from `system_audits.csv`, while child nodes are populated with random Base64 encoded strings (60-180 characters). |
| **Static Tables**           | `addresses.csv`, `cameras.csv`, and `safety_controls.csv` bypass procedural generation and are copied directly from the seed files. |

## Modelling

The data generation pipeline relies on a combination of stochastic processes, temporal bounded constraints, and hierarchical topological models to simulate realistic behavior for a metropolis of **186,377** baseline citizens over a 7.5-year simulation period.

### 1. Population Scale and Selection Probability

The simulation grounds its events in a baseline citizen pool, denoted as $P_{\text{base}} = 186,377$. For routine city events (e.g., taxi rides, standard camera sightings), the participating citizen is selected uniformly at random. The probability $P(C_i)$ of any specific citizen $i$ triggering a standard event at a given timestamp is:
$$
P(C_i) = \frac{1}{P_{\text{base}}}
$$
However, access-restricted events (Card Swipes) target a heavily filtered sub-population. The simulation restricts access to $N_{\text{permit}} = 234$ individuals (233 citizens with a social credit > 50, plus the Mayer). This isolates restricted movements to a fractional elite representing approximately **0.125%** of the total population.

### 2. Temporal Event Volumes (Poisson Point Processes)

Most system logs are modeled as Poisson point processes, where the continuous time interval between consecutive events follows an exponential distribution. Let $T_{\text{total}}$ represent the total elapsed time in seconds for a specific simulation phase, and $\beta$ represent the scale parameter (mean seconds between events). The expected total number of generated records, $E[N]$, over a given period is:
$$
E[N] = \frac{T_{\text{total}}}{\beta}
$$
By computing the exact time deltas between the defined start dates and the `CURRENT_DATETIME` (June 28, 2077), we can model the expected data volume for each table:

- **Long-Term Phase (Jan 1, 2070 – Jun 28, 2077):**

  Spans exactly 2,735 days (accounting for leap years in 2072 and 2076), which equals $T_{\text{long}} = 236,304,000$ seconds.

  - **Guard Logs:** ($\beta = 500$) $\rightarrow E[N] \approx 472,608$ records.
  - **Card Swipes:** ($\beta = 185$) $\rightarrow E[N] \approx 1,277,318$ records. Given the restricted pool of 234 permitted cards, this models a high-frequency access rate of roughly 2 routine swipes per permitted citizen per day.

- **Short-Term Phase (Jan 1, 2077 – Jun 28, 2077):**

  Spans exactly 178 days, equaling $T_{\text{short}} = 15,379,200$ seconds.

  - **Taxi Logs:** ($\beta = 10$) $\rightarrow E[N] \approx 1,537,920$ records.
  - **Camera Logs (Normal):** ($\beta = 20$) $\rightarrow E[N] \approx 768,960$ records.

### 3. Energy Center Subsystem (Gaussian Bounded Duration)

The Energy Center anomaly injects grouped pairs of camera logs (entry and exit). Events trigger with a sparse scale of $\beta = 6000$ over a 169-day window (ending June 19, 2077).

When a citizen enters, their duration $\Delta t_{\text{stay}}$ is determined by a bounded Gaussian (normal) distribution to simulate human dwell time:
$$
\Delta t_{\text{stay}} = \max\left(t_{\text{min}}, \mathcal{N}(\mu, \sigma^2)\right)
$$
With $\mu = 48,000$ (approx. 13.3 hours), $\sigma = 16,000$ (approx. 4.4 hours), and a hard minimum threshold $t_{\text{min}} = 1,000$ seconds (approx. 16.6 minutes). This ensures that ~99.7% of stays fall between 0 and 26.6 hours, organically modeling working shifts or prolonged detentions.

### 4. Hierarchical Audit Tree Growth

The internal system audits (`system_audits_inner.csv`) are mapped as an $n$-ary tree to simulate deep, nested system traces.

- **Root Nodes:** 30 quarterly meetings $\times$ 3 prompts = 90 root nodes.

- **Tree Topology:** The depth is strictly $D = 4$, with a branching array $C = [2, 3, 2, 3]$. The total node count $N_{\text{nodes}}$ generated per root is computed iteratively:
  $$
  N_{\text{nodes}} = 1 + \sum_{i=1}^{D} \prod_{j=1}^{i} C_j
  $$
  Calculating the specific constants: $1 + (2) + (2 \times 3) + (2 \times 3 \times 2) + (2 \times 3 \times 2 \times 3) = 1 + 2 + 6 + 12 + 36 = \textbf{57 nodes per tree}$.

  Across 90 root meetings, this deterministic model guarantees exactly **5,130** cryptographically obfuscated inner audit logs.

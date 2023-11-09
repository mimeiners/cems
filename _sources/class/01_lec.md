<!-- !split -->
<!-- jupyter-book 01_lec.md -->
# Introduction and Survey

<!-- !split -->
### Course Objectives
* Interfacing Microsystems
  * Mixed-technology VLSI systems (System-on-Chip, SoC)

* Design Methodology
  * Seamlessly modeling and design over all physical domains 

* Concept Engineering ASICs
  * Partitioning
  * Packaging


<!-- !split -->
### Scientific Computing / Data Science
* [Python](https://www.anaconda.com/download/)
* [Matlab](http://de.mathworks.com/?requestedDomain=de.mathworks.com)
* [Command-line tools](https://jeroenjanssens.com/seven/) 

<!-- !split -->
### Circuit Simulation
* [LTspice (Analog Devices)](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)
* [TINA-TI (Texas Instruments)](https://www.ti.com/tool/TINA-TI)
* [ngspice (Open Source)](http://ngspice.sourceforge.net)
* [ELDO (SiemensEDA)](https://eda.sw.siemens.com/en-US/eldo/)
* [Spectre (CADENCE)](https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/circuit-simulation/spectre-simulation-platform.html)
* [PrimeSim HSPICE (SYNOPSIS)](https://www.synopsys.com/implementation-and-signoff/ams-simulation/primesim-hspice.html)

<!-- !split -->
### OS Tools
  * [Shell](https://en.wikipedia.org/wiki/Shell_%28computing%29)
    * [oh-my-zsh](https://ohmyz.sh),
    * [bash-it](https://bash-it.readthedocs.io/en/latest/)
    * [SSH (Secure Shell)](https://de.wikipedia.org/wiki/Secure_Shell)

  * [GIT (Versionskontrolle)](https://git-scm.com)
  * [Cygwin](https://cygwin.com)
    * A large collection of GNU and Open Source tools which provide functionality similar to a Linux distribution on Windows.


<!-- !split -->
### Code Editors
* [Visual Studio Code](https://code.visualstudio.com)
* [Emacs](https://www.gnu.org/software/emacs/)
* [Vim](https://www.vim.org)

<!-- !split -->
### Data Science
* Folder in your filesystem (sandboxing, virtualenv)
* Table data: Comma-Separated-Values (CSV), Spreadsheet (.xlsx, .ods)
* Specific formats, e.g. MATLAB mat, HDF5
* Embedded [Databases](https://db-engines.com)
  * [SQL](https://en.wikipedia.org/wiki/SQL), e.g. [SQlite](https://en.wikipedia.org/wiki/SQLite)
  * [Key-Value](https://en.wikipedia.org/wiki/Key–value_database), e.g. [LevelDB](https://en.wikipedia.org/wiki/LevelDB)
  * [OLAP](https://en.wikipedia.org/wiki/Online_analytical_processing), e.g. [DuckDB](https://duckdb.org/why_duckdb)
  * [PythonDBs](https://www.opensourceforu.com/2017/05/three-python-databases-pickledb-tinydb-zodb/)
    * [PicklDB](https://github.com/patx/pickledb), key-value
    * [TinyDB](https://github.com/msiemens/tinydb), document-oriented db
    * [ZODB](https://github.com/zopefoundation/ZODB), object-oriented db



<!-- !split -->
### Are your writing or TeXing?
* [MikTeX (Windows, MacOS, Linux)](https://miktex.org/)
* [MacTeX (MacOS)](https://www.tug.org/mactex/)
* [TeXLive (Linux)](http://tug.org/texlive/)

<!-- !split -->
### LaTeX Editors
* IDE's
  * [TeXStudio](http://www.texstudio.org)
  * [TeXMaker](http://www.xm1math.net/texmaker/)

* Collaborative Frameworks
  * [Overleaf, Online LaTeX](https://www.overleaf.com/)
  * [CoCalc - Online LaTeX](https://cocalc.com/doc/latex-editor.html)


<!-- !split -->
### Bibliography and LaTeX
* [Citavi im Detail > Titel exportieren > Export nach BibTeX](https://www1.citavi.com/sub/manual5/de/exporting_to_bibtex.html)
* [Citavi Exporting to BibTeX](https://www1.citavi.com/sub/manual5/en/exporting_to_bibtex.html)
* [Benutzerdefinierte BibTex-Keys mit Zotero | nerdpause](https://nerdpause.de/benutzerdefinierte-bibtex-keys-mit-zotero/)
* [Better BibTeX for Zotero](https://retorque.re/zotero-better-bibtex/index.html)
* [JabRef - Library Guide Univ. Melbourne](https://unimelb.libguides.com/c.php?g=565734\&p=3897117)

<!-- !split -->
### Design Project
*Model-Based Systems Engineering of an Inertial Sensor System (MBSE).* 
* Use different description
  * System level (MBSE with Matlab, Simulink and Python)
  * Circuit level (SPICE) with behavioural blocks, e.g. OTA and comparator
  * Hardware: [ESP8266 NodeMCU](https://randomnerdtutorials.com/getting-started-with-esp8266-wifi-transceiver-review/), [TIs ADS1115](https://www.ti.com/product/ADS1115), [ADs ADXL335](https://www.analog.com/en/products/adxl335.html)
  * [Arduino IDE](https://www.arduino.cc/en/software) C-Programming and/or [Thonny](https://thonny.org) and/or [Visual Studio Code](https://code.visualstudio.com) [Micropython](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware) 
  * Teams of 3 students



<!-- !split -->
### Design Project Flow
* Literature research in journals, professional (serious) internet forums (e.g. application notes of semiconductor companies) and library 
* Set-up bibliography, e.g. [JabRef](http://www.jabref.org), [Citavi](https://www.suub.uni-bremen.de/literatur-verwalten/refworks/citavi/)
* Concept of your system
  * Partitioning
  * Functions
  * Work packages

* Design, implementation and validation
  * Mathmatical description
  * SPICE modeling and simulation
  * Data analysis and validation


<!-- !split -->
### Assignments
*Lab and Lecture.* 
* **Lab Design Project**: 50%
* **Final Oral Exam/Project Presentation**: 50%



<!-- !split -->
### Course Prerequisites
* Fundamentals of linux operating systems 
* Fundamentals of microelectronics
  * Device physics and models
  * Transistor level analog circuits, elementary gain stages

* Fundamentals of analog CMOS circuit design
  * Operational amplifier
  * Active filter design
  * Noise analysis
  * Switched-capacitor techniques

* Prior exposure to SPICE, Matlab, Python or equivalent.
* Please talk to me if you are not sure, if you have the required background.

<!-- !split -->
### Brave New World
<!-- !bslidecell 00 0.9 -->
<!-- <img src="../../lecture/doconce/fig/lec1_AMD@16nm@Jaguar.jpg" width="400"><p><em>AMD Jaguar APU (CPU/GPU), 16 nm, 325 qmm, 2016 <div id="fig:jaguar"></div></em></p> -->
![<p><em>AMD Jaguar APU (CPU/GPU), 16 nm, 325 qmm, 2016 <div id="fig:jaguar"></div></em></p>](../../lecture/doconce/fig/lec1_AMD@16nm@Jaguar.jpg)
<!-- !eslidecell -->

<!-- !split -->
### From Sand to Silicon (Infineon, Dresden)
<!-- !bslidecell 00 0.9 -->

<iframe width="793" height="446" src="https://www.youtube.com/embed/bor0qLifjz4?list=PLO_wT97BGA6xC6hNy9VGtt1bKwVuQXI5B" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### Sand to Silicon (GlobalFoundries, Desden)
<!-- !bslidecell 00 0.9 -->

<iframe width="793" height="446" src="https://www.youtube.com/embed/UvluuAIiA50?list=PLO_wT97BGA6xC6hNy9VGtt1bKwVuQXI5B" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### FinFET (Intel)
<!-- !bslidecell 00 0.9 -->

<iframe width="793" height="446" src="https://www.youtube.com/embed/_VMYPLXnd7E" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### TSMC Fab (Next Gen 7/5 nm)
<!-- !bslidecell 00 0.9 -->

<iframe width="793" height="446" src="https://www.youtube.com/embed/Hb1WDxSoSec" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### Once upon a time ...
<!-- !bslidecell 00 0.45 -->
<!-- <img src="../../lecture/doconce/fig/lec1_vacuum_tube.png" width="400"><p><em>1906 Electron Tube</em></p> -->
![<p><em>1906 Electron Tube</em></p>](../../lecture/doconce/fig/lec1_vacuum_tube.png)
<!-- !eslidecell -->

<!-- !bslidecell 01 0.45 -->
<!-- <img src="../../lecture/doconce/fig/lec1_1st_transistor.png" width="400"><p><em>1947 1st Transistor, Bell Labs</em></p> -->
![<p><em>1947 1st Transistor, Bell Labs</em></p>](../../lecture/doconce/fig/lec1_1st_transistor.png)
<!-- !eslidecell -->

<!-- !split -->
### First IC and today's chips
<!-- !bslidecell 00 0.45 -->
<!-- <img src="../../lecture/doconce/fig/lec1_1st_ic_kilby.png" width="400"><p><em>1958 Jack Kilby's 1st IC <div id="fig:kilbyic"></div></em></p> -->
![<p><em>1958 Jack Kilby's 1st IC <div id="fig:kilbyic"></div></em></p>](../../lecture/doconce/fig/lec1_1st_ic_kilby.png)
<!-- !eslidecell -->

<!-- !bslidecell 01 0.45 -->
<!-- <img src="../../lecture/doconce/fig/lec1_modern_ic.png" width="400"><p><em>Moderner IC <div id="fig:modernic"></div></em></p> -->
![<p><em>Moderner IC <div id="fig:modernic"></div></em></p>](../../lecture/doconce/fig/lec1_modern_ic.png)
<!-- !eslidecell -->

<!-- !split -->
### Packaging Densities
<!-- !bslidecell 00 0.85 -->
<!-- <img src="../../lecture/doconce/fig/lec1_wafers.png" width="600"><p><em>Wafer generations <div id="fig:wafer"></div></em></p> -->
![<p><em>Wafer generations <div id="fig:wafer"></div></em></p>](../../lecture/doconce/fig/lec1_wafers.png)
<!-- !eslidecell -->

<!-- !split -->
### Moore's Law
<!-- !bslidecell 00 0.9 -->


<embed src="https://players.brightcove.net/734546229001/default_default/index.html?videoId=4144803153001" width="793" height="446" autoplay="false" loop="true"></embed>
<p><em></em></p>


<!-- !eslidecell -->

<!-- !split -->
### System Hierarchy
<!-- !bslidecell 00 0.75 -->
<!-- <img src="../../lecture/doconce/fig/lec1_system_hierarchy.png" height="400"><p><em>Blocks of an electronic system. <div id="fig:hierarchy"></div></em></p> -->
![<p><em>Blocks of an electronic system. <div id="fig:hierarchy"></div></em></p>](../../lecture/doconce/fig/lec1_system_hierarchy.png)
<!-- !eslidecell -->

* Use hierarchy to descibe complex systems
* Devide and conquere

<!-- !split -->
### System Assembly

<!-- <img src="../../lecture/doconce/fig/lec1_system_assembly.png" height="400"><p><em>Bottom-up Prozess, Integration. <div id="fig:assembly"></div></em></p> -->
![<p><em>Bottom-up Prozess, Integration. <div id="fig:assembly"></div></em></p>](../../lecture/doconce/fig/lec1_system_assembly.png)

<!-- !split -->
### Interfacing

<!-- <img src="../../lecture/doconce/fig/lec1_real_world_interface.png" width="400"><p><em>Interfacing. <div id="fig:interfaces"></div></em></p> -->
![<p><em>Interfacing. <div id="fig:interfaces"></div></em></p>](../../lecture/doconce/fig/lec1_real_world_interface.png)

<!-- !split -->
### Meeting a System (1)

<!-- <img src="../../lecture/doconce/fig/lec1_smartphone.png" width="400"><p><em>Wireless Communication System. <div id="fig:smartphone"></div></em></p> -->
![<p><em>Wireless Communication System. <div id="fig:smartphone"></div></em></p>](../../lecture/doconce/fig/lec1_smartphone.png)

<!-- !split -->
### System in a Package (SiP)

<!-- <img src="../../lecture/doconce/fig/lec1_system_in_package.png" width="400"><p><em>Accelerometer. <div id="fig:sip"></div></em></p> -->
![<p><em>Accelerometer. <div id="fig:sip"></div></em></p>](../../lecture/doconce/fig/lec1_system_in_package.png)

<!-- !split -->
### You will become an expert
*Indicators.* 
* Background Knowledge
  * System Knowledge, Architecture, Processing, Implementation

* Subconscious Knowledge
  * Memorized experiences of success stories and dead ends

* Special Knowledge
  * Dicipline related knowledge, e.g. physics, hardware, software

* Teamwork
  * Communication abilities, reporting and presentation

* Creativity
* Tool-Knowlege



<!-- !split -->
### Views on Hardware (1)

<!-- <img src="fig/lec1_views_on_hardware_1.png" width="400"> -->
![](fig/lec1_views_on_hardware_1.png)

<!-- !split -->
### Views on Hardware (2)

<!-- <img src="../../lecture/doconce/fig/lec1_views_on_hardware_2.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec1_views_on_hardware_2.png)

<!-- !split -->
### Abstraction Layer

<!-- <img src="../../lecture/doconce/fig/lec1_abstraction_layer.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec1_abstraction_layer.png)

<!-- !split -->
### Design Flow

<!-- <img src="../../lecture/doconce/fig/lec1_design_flow.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec1_design_flow.png)

<!-- !split -->
### Verification

<!-- <img src="../../lecture/doconce/fig/lec1_verification.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec1_verification.png)

<!-- !split -->
### Frontend vs. Backend (analog)

<!-- <img src="../../lecture/doconce/fig/lec1_front-end_back-end_analog.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec1_front-end_back-end_analog.png)

<!-- !split -->
### Frontend vs. Backend (digital)

<!-- <img src="../../lecture/doconce/fig/lec1_front-end_back-end_digital.png" width="400"><p><em>(c) M. Ortmanns, Univ. Ulm.</em></p> -->
![<p><em>(c) M. Ortmanns, Univ. Ulm.</em></p>](../../lecture/doconce/fig/lec1_front-end_back-end_digital.png)

<!-- !split -->
### Analog Design Entry

<!-- <img src="fig/lec1_design_entry_analog.png" width="400"> -->
![](fig/lec1_design_entry_analog.png)

<!-- !split -->
### Netlist

<!-- <img src="fig/lec1_netlist.png" width="400"> -->
![](fig/lec1_netlist.png)

<!-- !split -->
### Layout

<!-- <img src="fig/lec1_inverter_layout.png" width="400"> -->
![](fig/lec1_inverter_layout.png)

<!-- !split -->
### Digital Design Entry

<!-- <img src="fig/lec1_design_entry_digital.png" width="400"> -->
![](fig/lec1_design_entry_digital.png)

<!-- !split -->
### Hardware Desciption Language

<!-- <img src="fig/lec1_hdl_inv.png" width="400"> -->
![](fig/lec1_hdl_inv.png)

<!-- !split -->
### Technology-Gates and Netlisting

<!-- <img src="fig/lec1_technology_gate_netlist.png" width="400"> -->
![](fig/lec1_technology_gate_netlist.png)

<!-- !split -->
### Standard Cell Layout

<!-- <img src="fig/lec1_standard_cell_layout.png" width="400"> -->
![](fig/lec1_standard_cell_layout.png)

<!-- !split -->
### Sustainable Electronics ...
<!-- !bslidecell 00 0.9 -->

<iframe width="859" height="483" src="https://www.youtube.com/embed/7S5IuaKiZIY" frameborder="0" allowfullscreen></iframe>

<p><em>Geekchester.</em></p>


<!-- !eslidecell -->

<!-- !split -->
### Why it is worth ...
<!-- !bslidecell 00 0.9 -->

<iframe width="859" height="483" src="https://www.youtube.com/embed/SwPGxwBZw6I" frameborder="0" allowfullscreen></iframe>

<p><em>Circuit Song.</em></p>


<!-- !eslidecell -->

<!-- !split -->
### Let's go to the beach ...
<!-- !bslidecell 00 0.9 -->

<iframe width="859" height="483" src="https://www.youtube.com/embed/ekkJlQf-K4I" frameborder="0" allowfullscreen></iframe>

<p><em>Viva la Electronica.</em></p>


<!-- !eslidecell -->

<!-- !split -->

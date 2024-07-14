<!-- !split -->
<!-- jupyter-book 02_lec.md -->
# Systems Engineering for Gyros

<!-- !split -->
### Vehicles without ESP

<!-- <img src="../../lecture/doconce/fig/lec2_moose.png" width="400"><p><em>The moose test / elk test. <div id="fig:elk-test"></div></em></p> -->
![<p><em>The moose test / elk test. <div id="fig:elk-test"></div></em></p>](../../lecture/doconce/fig/lec2_moose.png)

<!-- !split -->
### Vehicle Dynamics Controls Systems - ESP

<!-- <img src="../../lecture/doconce/fig/lec2_esp.png" width="400"><p><em>Market launch of gyros. <div id="fig:market-launch"></div></em></p> -->
![<p><em>Market launch of gyros. <div id="fig:market-launch"></div></em></p>](../../lecture/doconce/fig/lec2_esp.png)

<!-- !split -->
### Consumer Gyroscopes

*Market segments.* 
* Mobile phones
* Digital cameras
* Pointing devices
* Gaming consoles
* GPS portables



<!-- <img src="./fig/lec2_ipad.png" width="300"> -->
![](./fig/lec2_ipad.png)

<!-- <img src="./fig/lec2_samsung.png" width="200"> -->
![](./fig/lec2_samsung.png)

<!-- <img src="./fig/lec2_garmin.png" width="300"> -->
![](./fig/lec2_garmin.png)

<!-- <img src="./fig/lec2_ixus.png" width="200"> -->
![](./fig/lec2_ixus.png)

<!-- <img src="./fig/lec2_wii.png" width="300"> -->
![](./fig/lec2_wii.png)

<!-- !split -->

### MEMS for Automotive and Consumer Applications


<iframe width="640" height="365" src="https://www.youtube.com/embed/5MKnlsLtK34" frameborder="0" allowfullscreen></iframe>

<p><em>Plenary Sessions from the 2010 ISSCC</em></p>



* Jiri Marek, Senior Vice President, Robert Bosch, Reutlingen, Germany

<!-- !split -->
### MEMS Gyroscope in Action


<div>
<video loop controls width='640' height='365' preload='none'>
    <source src='../../lecture/doconce/mov/lec2_mm3drive.mp4'  type='video/mp4;  codecs="avc1.42E01E, mp4a.40.2"'>
</video>
</div>
<p><em>Drive movement as model animation.</em></p>

<!-- Issue warning if in a Safari browser -->
<script language="javascript">
if (!!(window.safari)) {
  document.write("<div style=\"width:95%%; padding:10px; border:1px solid #100; border-radius:4px;\"><p><font color=\"red\">The above movie will not play in Safari - use Chrome, Firefox, or Opera.</font></p></div>")}
</script>




<div>
<video loop controls width='640' height='365' preload='none'>
    <source src='../../lecture/doconce/mov/lec2_mm3sense.mp4'  type='video/mp4;  codecs="avc1.42E01E, mp4a.40.2"'>
</video>
</div>
<p><em>Sense movement as model animation.</em></p>

<!-- Issue warning if in a Safari browser -->
<script language="javascript">
if (!!(window.safari)) {
  document.write("<div style=\"width:95%%; padding:10px; border:1px solid #100; border-radius:4px;\"><p><font color=\"red\">The above movie will not play in Safari - use Chrome, Firefox, or Opera.</font></p></div>")}
</script>



<!-- !split -->
### Spring-Mass-Damping System

* 1-D equation of motion (EoM) $F = m\ddot{x} + d\dot{x} + kx$
* Laplace transformation

$$
\begin{align}
H(s) &= \frac{1}{m s^2 +  d s + k} \\
     &= \frac{\frac{1}{m}}{s^2 + \frac{\omega_0}{Q} s + \omega_0^2}
\end{align}
$$

<!-- !split -->
### Functional Block Diagram
<!-- <img src="./fig/lec2_gyroblock.png" width="300"> -->
![](./fig/lec2_gyroblock.png)

* Coriolis force principle, $F_C = 2 m \left(\mathbf{v} \times \Omega \right)$
* Drive loop to have an accelerated mass
* Sense loop to detect angular rate
* Distinction of closed-loop and open-loop system

<!-- !split -->
### Multi-Domain Readout Block Diagram
<!-- <img src="./fig/lec2_sdsystem.png" width="300"> -->
![](./fig/lec2_sdsystem.png)

$$
\begin{align}
H_s(s) &= \frac{\frac{1}{m}}{s^2 + \frac{\omega_0}{Q}s + \omega_0^2} &\quad \mbox{sensor} \\
H_{CV}(s) &= \frac{g_m}{C_L}\frac{1-e^{-sT_{int}}}{s} &\quad \mbox{CV converter} \\
H_{lf}(z) &= -\frac{z}{z+a}\frac{z^2 +b_1z +b_0}{z^2 +c_1z +c_0} &\quad \mbox{loop filter}
\end{align}
$$

<!-- !split -->
### Multi-Domain Modelling

* Describing kinematic and electrical behaviour with the help of HDL
  * VHDL, VHDL-AMS
  * Verilog, Verilog-A, Verilog-AMS

* Using ROM for a MATLAB/SIMULINK model and real-time workshop to port model for use with Cadence $\rightarrow$ Verilog-AMS is used for wrapping
* Parasitic SPICE circuit equivalent from FEM sensor model and layout extraction

<!-- !split -->
### ROM Modelling - Coordinate transformation
<!-- <img src="./fig/lec2_rom.png" width="300"> -->
![](./fig/lec2_rom.png)

$$
\begin{align}
    M \ddot{x} &+ K x &= F &\quad \mbox{FEM, 100.000 DOF}\\
    M \phi \ddot{q} &+ K \phi q &= F & \\
    \underbrace{\phi' M \phi} \ddot{q} &+ \underbrace{\phi' K \phi} q &= \phi' F & \\
    \tilde{M} \ddot{q} &+ \tilde{K} q &= \tilde{F} & \quad \mbox{ROM, approx. 10 DOF}
\end{align}
$$

<!-- !split -->
### Gyro Behavioural Modelling

<!-- <img src="../../lecture/doconce/fig/lec2_gyromodel.png" height="400"><p><em>Model of gyroscope.</em></p> -->
![<p><em>Model of gyroscope.</em></p>](../../lecture/doconce/fig/lec2_gyromodel.png)

<!-- !split -->
### Mixed-domain simulation
* All models from previous slide can be used in Cadence design frame work
* Pure analog closed-loop transient simulation with Spectre (turbo, aps), circuits and verilog-a model
* Pure analog closed-loop simulation with SPICE circuit equivalent
* Mixed-domain, mixed-mode simulation with AMSDesigner (ncsim, spectre-turbo/aps)

<!-- !split -->
### Analog Closed-Loop Simulation

<!-- <img src="../../lecture/doconce/fig/lec2_analogsim.png" height="400"><p><em>Analog simulation with Cadence.</em></p> -->
![<p><em>Analog simulation with Cadence.</em></p>](../../lecture/doconce/fig/lec2_analogsim.png)

<!-- !split -->
### AMS Closed-Loop Simulation

<!-- <img src="../../lecture/doconce/fig/lec2_amssim.png" width="400"><p><em>AMS simulation with Cadence.</em></p> -->
![<p><em>AMS simulation with Cadence.</em></p>](../../lecture/doconce/fig/lec2_amssim.png)

<!-- !split -->
### Conclusion
*Vibratory Gyroscopes.* 
* Automotive and consumer applications
* System architectures
* Mixed-domain, mixed-mode analysis
* Interdisciplinarity $\rightarrow$ IC Systems Engineering  Control theory, signal theory, process technology and micromechanics



*More DOF’s.* 
* Acceleration and angular rate (6 DOF’s)
* Angulare rate and magneto sensors (6 DOF’s)
* Acceleration, angular and magneto (9 DOF’s)



<!-- !split -->

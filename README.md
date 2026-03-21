\# EDA



\- Performed end-to-end exploratory data analysis on a \*\*3,600-record wind turbine sensor dataset\*\* covering 14 operational features including thermal, mechanical, and environmental readings.

&#x20;   - Why this works: Establishes scope immediately - 3,600 records, 14 features, real sensor data. Hiring managers can picture the project without asking follow-up questions. Avoid just saying “performed EDA on a dataset.”

\- Conducted univariate and bivariate analysis including distribution plots, boxplots, and correlation heatmaps to identify key failure indicators across sensor readings.



\# Insights



\- Identified that gear oil temperature above 100°C perfectly separates failure from normal operation (100% failure rate vs 0% below threshold), translating the finding into a rule-based operational alert without requiring a machine learning model.

\- Discovered that yaw angle (corr: 0.92) and gear oil temperature (corr: 0.90) are the dominant failure predictors, while nacelle temperature showed near-zero correlation — reducing feature space for modelling.

\- Defined a safe rotor operating band (100–250 RPM) with 0% failure rate, and flagged that both stall (<100 RPM) and overspeed (>250 RPM) conditions each contributed 50% of all recorded failures.

\- Found that failure events produce higher average power output (4.53 kW vs 2.78 kW normal), indicating turbine over-driving at extreme wind speeds rather than gradual degradation — reframing the maintenance hypothesis.



\# Final Dashboard Insights



\*\*4 KPI Cards (top row)\*\*



\- Gear oil temperature averages 114.78°C during failures vs 70.27°C during normal operation — a 44.5°C gap that directly points to gearbox overheating as the primary failure cause

\- Average wind speed during failure is 21.29 m/s, which is higher than normal — confirms turbines are more stressed at higher wind speeds

\- 33.33% failure rate means 1 in every 3 readings is a failure — unusually high, signaling a systemic maintenance problem



\*\*Count of Failure\_status by Season (clustered bar, bottom left)\*\*



\- Blue bars (failure) are consistently shorter than yellow bars (normal) across all 4 seasons

\- The ratio between blue and yellow is almost identical in every season — Spring, Summer, Autumn, Winter all show the same pattern

\- Business insight: seasonal maintenance schedules will not help — failures happen equally regardless of weather



\*\*Yaw Angle — Failure vs Normal (middle bar chart)\*\*



\- The failure bar stands at \~123° while normal sits nearly flat at \~13°

\- This is the most dramatic visual in your entire dashboard — the height gap is unmissable

\- Business insight: yaw misalignment beyond 60° is a near-certain failure predictor — install real-time yaw angle alerts



\*\*Failure vs Wind Speed \& Power Output (horizontal bar, top right)\*\*



\- The Failure bar extends much further on the Avg\_Gear\_oil\_temp axis than No\_failure

\- Confirms the KPI card finding visually — failure rows consistently have higher gear oil temperatures

\- Business insight: gear oil temperature threshold monitoring can serve as an early warning system



\*\*Failure Count and Normal Event (donut chart)\*\*



\- 1K failures (33.33%) vs 2K normal (66.67%) shown clearly

\- Simple and immediately readable — good anchor visual for any non-technical audience



\*\*Record Count by Month and Failure\_status (line chart)\*\*



\- Both lines are completely flat across all 12 months — failure count \~100/month, normal \~200/month every single month

\- Business insight: there is no seasonal spike, no month that is safer or more dangerous — the failure condition is permanent and continuous, not an event



\*\*%GT Record Count by Season and Failure\_status (100% stacked horizontal bar)\*\*



\- Each season shows the same blue-to-yellow split — approximately 33% blue and 67% yellow for every season

\- This is the strongest visual proof of the no-seasonality conclusion because all bars reach 100% so the comparison is perfectly fair

\- Business insight: if a maintenance team reads only one chart to decide whether to do seasonal servicing, this chart tells them not to bother — fix the sensors instead



\# Business Impact



\- Implementing these two threshold alerts as SCADA rules eliminates the need for a machine learning model for basic failure detection — saving model development cost while achieving 100% recall on this dataset.

\- Planned maintenance during the warning zone (70–100°C) is significantly cheaper than emergency repair after failure. The data shows a clear window — 1,224 records of run time — before the critical threshold is crossed.

\- Two separate control mechanisms are needed — a stall recovery protocol for low RPM and an overspeed governor for high RPM. Addressing only one would still leave 50% of rotor-related failures unprotected.

\- Maintenance budgets and crew scheduling can be directly tied to weather forecasts. Pre-positioning inspection teams before temperature extremes — rather than running fixed calendar-based maintenance — would cover 88% of failure-prone conditions proactively.


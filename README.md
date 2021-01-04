# tap-thunderboard
Collect data from Silicon Labs Thunderboard and output Singer messages.

Initially "Forked" from: https://www.silabs.com/community/projects.entry.html/2017/03/08/thunderboard_sensew-Scqr


## build

   ```
   make install
   ```

## run

To run non root
   ```
   sudo setcap cap_net_raw+e ./venv/bin/tap-thunderboard
   sudo setcap cap_net_admin+eip ./venv/bin/tap-thunderboard
   ./venv/bin/tap-thunderboard -s
   ```


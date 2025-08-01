# Changelog

#### 1.0.19

##### Chores

*  add bundle-types workflow (#1327) (ef3bc6df)

##### New Features

* **FieldsBreakdown:**  Show panels with errors (#1346) (7d0f70bc)
* **FieldValues:**  add better max series limit error message (#1345) (7f1df4cd)

##### Bug Fixes

* **datasources:**  default datasources (#1348) (b0842eab)

##### Refactors

* **changelog:**  manually fix changelog (#1342) (63333a8e)

##### Tests

*  hopeful flake fix (21c05825)


#### 1.0.18

##### Chores

* **gha:**
  *  id-token permission (#1338) (283b1fb2)
  *  update ci to ci/cd job to auto deploy to dev (#1321) (a600310f)
  *  github permissions are fun (#1314) (d650a4f1)
  *  add proper permissions to format gh issues (#1312) (118774d3)
  *  update deployment tools wf (#1297) (6ccbf550)
* **deps:**  bump golang.org/x/net (#1326) (b43e2320)
* **gh issues:**
  *  formate issues with labels and project (#1291) (8e4777c1)
  *  update issue templates (#1290) (ffe12ffb)

##### New Features

* **embedding:**
  *  Embedded readonly filters (#1315) (43abb74d)
  *  Embedded Service Scene Component (#1294) (bd4f5e36)
* **LogsPanelScene:**  pass custom items to new panel (#1306) (3d011c63)
*  add token to generator (#1305) (784f7764)

##### Bug Fixes

* **logs-panel:**  infinite scroll broken by double jsonFields interpolation (#1302) (97619800)
* **JSON:**  add second json parser stage (#1301) (20b338dd)
* **EmbeddedLogs:**  Prevent readonly filter removal (#1323) (39678dbe)

#### 1.0.17

##### Chores

* **gh issues:**
  *  format issues with labels and project (#1291) (8e4777c1)
  *  update issue templates (#1290) (ffe12ffb)
* **lint:**  lint all the things, except ignore (#1289) (5798dec4)

##### Bug Fixes

* **table:**  move sorting and remove initial sorting from table (#1284) (f0561406)

#### 1.0.16

##### Chores

*  Call interpolateExpression (#1276) (796cacee)
*  Run lint (#1274) (fa1d3b7d)
*  Update Grafana assets to 11.6.1 (#1270) (505a307a)
*  Add option to output to syslog from the generator (#1240) (14057e9f)
* **vault:**  Use vault, remove old gha (#1272) (b4b9a896)
* **plugin-ci-workflows:**
  *  Publish skip playwright (#1263) (5becc84a)
  *  Playwright skip dev image (#1262) (99ef2c9b)

##### Documentation Changes

*  Add favorites docs to readme (#1277) (cd64dbfc)
*  Dashboards > Visualizations (#1261) (216b9256)

#### 1.0.15

##### Chores

- (plugin-ci-workflows) - init vanilla plugin-ci-workflows (#1215) (ea21ded8)
- bump @grafana/create-plugin configuration to 5.19.8 (#1232) (9ffc46f6)
- **plugin-ci-workflows:** temporarily disable release.yml (#1256) (8517cc0f)
- **bundle-stats:** swap bundlewatch for cp gha bundle-stats (#1252) (2121df39)
- **e2e:** clean up & flake prevention (#1247) (0ee52382)
- **eslint:** sort, a11y, cleanup husky, lint (#1219) (f3505456)

##### Documentation Changes

- Updating screenshots and docs (#1248) (a1db542d)
- update the versions in the README (#1249) (6f4c3c48)
- JSON viewer documentation (#1243) (a78469d9)

##### Bug Fixes

- Fix field filters causing fields to disappear from table & logs panel (#1253) (f8882f08)
- **aggregated-metric:** Dropdown broken on click (#1246) (bf4f021d)
- **links:** Single escaped doublequote bug (#1242) (cd8168ac)

## 1.0.14

##### Chores

- **docker-compose:** update loki to 3.5.0 (#1235) (a1a763c3)
- add a few fixes to the logs needed for the GrafanaCon talk (#1231) (02661080)
- update version check for controls (#1220) (7fa43723)
- otel generator changes (#1206) (60738a68)
- add changelog (ac81678c)
- **zizmor:** update for template-injection (#1222) (e565937a)
- **gh actions:** check pr titles for conventional commits (#1218) (8d6f25df)

##### New Features

- Use new Log Controls component (#1204) (a58e2762)
- JSON Viz (#1209)" (#1210) (5e014e98)
- support numeric operators for int fields (#1227) (4f4b7981)

##### Bug Fixes

- **line-filters:** Expand no longer working. (#1238) (1dbbb75d)
- Empty results layout in JSON and Table (#1236) (beb9489e)
- Panel menu visibility in json (#1216) (af1ed41a)
- JSON - line format containing unsupported chars (#1214) (c2c8bf23)
- **table:** missing line filter (#1237) (a1a4ea82)
- **zizmor:** fix conventional-commits error (#1229) (93cc282c)

## 1.0.13

##### Bug Fixes

- Fix issue with release pipeline

## 1.0.12

##### Chores

- Remove `ToolbarExtensionsRenderer` (#1187) (ba7383ac)
- (Provisioning) - Add loki datasource and env (#1175) (9d319574)
- (Grafana 11.6) - Update to latest grafana 11.6 and latest plugin libraries, remove comments (#1162) (d8edbcb5)
- Updating to Scenes v6 (#1019) (a13d9e21)
- Conditionally display "show logs" buttons (#1194) (fad95388)
- Simplify panel buttons (#1188) (37c50063)

##### New Features

- (LogPanelTable) - Sync the display fields and urlColumns between the logs panel and table (#1189) (139c5803)
- (LayoutSwitcher) - Set layoutSwitcher from localStorage (#1172) (df7454e3)
- Line filter validation (#1190) (f38aa5fd)

##### Bug Fixes

- Patterns table displaying percentage relative to current search results (#1186) (f3bb1fe4)
- ParseLabelFilters throw error (#1181) (72378ff9)
- Fix url sharing and line filter migrations (#1176) (7c2ecb77)

## 1.0.11

##### Chores

- (gh actions) - pin to tag for security (#1173) (a58f29ec)
- Bump @grafana/create-plugin configuration to 5.19.1 (#1159) (ae36050c)
- Fix e2e test (#1135) (7873d6dd)

##### Documentation Changes

- Update readme to include discover_log_levels config requirement (#1143) (359e9766)

##### New Features

- Add critical/fatal log level (#1146) (038a8146)
- Add support for uppercase log level and color warning as a warn (#1137) (4675f4a7)

##### Bug Fixes

- Links should use `firstValueFrom` (#1170) (7caf11c8)
- Changelog (#1169) (c662e796)
- Error being thrown when toggling case sensitivity with empty value (#1153) (156245c9)
- Set step as 10s for aggregated metric queries (#1145) (b370c190)

##### Other Changes

- Remove padding and combine level with fields (#1168) (977a839d)
- Make extensions compatibly with different Grafana versions (#1148) (e2c75d29)

## 1.0.10

##### Chores

- Fix e2e test (#1135) (7873d6dd)

##### Documentation Changes

- Update readme to include discover_log_levels config requirement (#1143) (359e9766)

##### New Features

- Add critical/fatal log level (#1146) (038a8146)
- Add support for uppercase log level and color warning as a warn (#1137) (4675f4a7)

##### Bug Fixes

- Error thrown when toggling case sensitivity with an empty value (#1153) (156245c9)
- Set step as 10s for aggregated metric queries (#1145) (b370c190)

##### Other Changes

- Make extensions compatibly with different Grafana versions (#1148) (e2c75d29)


View [releases](https://github.com/grafana/explore-logs/releases/) on GitHub for up-to-date changelog information.

## 1.0.9

##### New Features

- Value drilldown UX: Multiple include filters (https://github.com/grafana/explore-logs/pull/1074)
- Service selection pagination: generate options based on totalCount (https://github.com/grafana/explore-logs/pull/1077)
- Display error message when logs fail to load (https://github.com/grafana/explore-logs/pull/1079)
- No Loki datasource splash page: (https://github.com/grafana/explore-logs/pull/1061)
- Navigation UX: Open pages in new tab (https://github.com/grafana/explore-logs/pull/1106)
- Table UX: surface field menu options in column header (https://github.com/grafana/explore-logs/pull/1064)
- Table UX: Add Manage columns button to table header (https://github.com/grafana/explore-logs/pull/1057)
- Line filters UX: expand input on focus (https://github.com/grafana/explore-logs/pull/1113)
- Service Scene UX: Pagination (https://github.com/grafana/explore-logs/pull/1058)
- Link extensions: Open in Explore logs button (https://github.com/grafana/explore-logs/pull/1035)
- Link extensions: Add pattern filter support (https://github.com/grafana/explore-logs/pull/1036)
- Link extensions: Support multiple include filters in queries from Explore (https://github.com/grafana/explore-logs/pull/1103)

##### Bug Fixes

- Empty label values missing labelValues (https://github.com/grafana/explore-logs/pull/1111)
- Move share button to right side on mobile (https://github.com/grafana/explore-logs/pull/1115)
- Clear filters icon not working with detected_level (https://github.com/grafana/explore-logs/pull/1105)
- Add overflow-y to tabs container (https://github.com/grafana/explore-logs/pull/1104)
- ServiceSelectionPagination: check for undefined in options (https://github.com/grafana/explore-logs/pull/1080
- Cannot add more then 2 values for same label (https://github.com/grafana/explore-logs/pull/1088)
- Allow direction to be updated when sort order changes (https://github.com/grafana/explore-logs/pull/1082)

##### Chores

- Increase loki max log length (https://github.com/grafana/explore-logs/pull/1112)
- Add missing image, remove empty section (https://github.com/grafana/explore-logs/pull/1089)
- Make OTEL endpoint configurable in generator dockerfile (https://github.com/grafana/explore-logs/pull/1075)
- Rename: rename exposed component (https://github.com/grafana/explore-logs/pull/1094)
- Add metadata to logged error (https://github.com/grafana/explore-logs/pull/1129)

##### Documentation Changes

- Fix title copy (https://github.com/grafana/explore-logs/pull/1092)

##### Other Changes

- Add `fieldConfig` to investigations context (https://github.com/grafana/explore-logs/pull/1124)
- Investigations: change investigations plugin id (https://github.com/grafana/explore-logs/pull/1084)
- E2E flake (https://github.com/grafana/explore-logs/pull/1101)

## 1.0.8

- Open in Explore logs button by @kozhuhds in https://github.com/grafana/explore-logs/pull/1035
- Table: Add manage columns button to table header by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1057
- Table: Hide custom pixel width, surface field menu options in column header by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1064
- Service selection: Pagination by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1058
- Make OTEL endpoint configurable in generator dockerfile by @shantanualsi in https://github.com/grafana/explore-logs/pull/1075
- Service Selection Pagination: Generate options based on total count by @matyax in https://github.com/grafana/explore-logs/pull/1077
- Service Selection Pagination: Check for possibly undefined in options by @matyax in https://github.com/grafana/explore-logs/pull/1080
- Explore links: Add pattern filter support by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1036
- Logs Panel: Display error message when logs fail to load by @matyax in https://github.com/grafana/explore-logs/pull/1079
- Docs: Migrate images to media service by @robbymilo in https://github.com/grafana/explore-logs/pull/1081
- Query runner: Allow direction to be updated when sort order changes by @matyax in https://github.com/grafana/explore-logs/pull/1082
- Investigations: change investigations plugin id by @svennergr in https://github.com/grafana/explore-logs/pull/1084
- Grafana Drilldown Logs by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1054
- Labels combobox: Cannot add more then 2 values for same label by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1088
- README: Fix missing image, empty section by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1089
- No loki datasource: Splash page by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1061
- Fix splash page relative URL, update img in readme by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1090
- Docs: Fix title copy by @knylander-grafana in https://github.com/grafana/explore-logs/pull/1092

## 1.0.7

- Link extensions: Add support for line filters by @gtk-grafana in https://github.com/grafana/explore-logs/pull/997
- Link extensions: Add support for fields by @gtk-grafana in https://github.com/grafana/explore-logs/pull/999
- Patterns: Patterns containing quotes break when added as filter by @gtk-grafana in https://github.com/grafana/explore-logs/issues/1003
- Service Selection: make volume search case-insensitive by @gtk-grafana in https://github.com/grafana/explore-logs/issues/1012
- Regex labels: Support queries from explore by @gtk-grafana in https://github.com/grafana/explore-logs/issues/1010
- Table: Open in Explore links do not add labelFieldName by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1018
- Patterns: Not configured state not working by @gtk-grafana in https://github.com/grafana/explore-logs/issues/1021
- Fields: Regex by @gtk-grafana in https://github.com/grafana/explore-logs/pull/1023
- Logs Volume: Set axis soft min of 0 by @gtk-grafana in https://github.com/grafana/explore-logs/issues/1041
- Logs: Apply query direction in query runner by @matyax in https://github.com/grafana/explore-logs/pull/1047
- Filters: Expression builder - differentiate user input from selected tags/values by @gtk-grafana in https://github.com/grafana/explore-logs/issues/1045
- Upgrade scenes to prevent panels from not being hidden by @svennergr in https://github.com/grafana/explore-logs/issues/1025

## 1.0.6

- Line filters: Regex support by @gtk-grafana in https://github.com/grafana/explore-logs/pull/963
- Line filters: Allow backticks5 by @gtk-grafana in https://github.com/grafana/explore-logs/pull/992
- Fix: use urlUtil instead of UrlSearchParams by @gtk-grafana in https://github.com/grafana/explore-logs/pull/994
- Sorting: prevent sorting timeFields in place by @svennergr in https://github.com/grafana/explore-logs/pull/996

## 1.0.5

- feat(explorations): remove disabled state by @svennergr in https://github.com/grafana/explore-logs/pull/913
- Webpack: upgrade to 5.95 by @gtk-grafana in https://github.com/grafana/explore-logs/pull/914
- chore: cleanup faro error messages by @gtk-grafana in https://github.com/grafana/explore-logs/pull/915
- Logs Panel: move log panel options and add sort order by @gtk-grafana in https://github.com/grafana/explore-logs/pull/920
- Panel Menus by @gtk-grafana in https://github.com/grafana/explore-logs/pull/892
- fix(firefox-panel-hidden): add position absolute by @svennergr in https://github.com/grafana/explore-logs/pull/928
- SortLevelTransformation: account for possibly empty fields by @matyax in https://github.com/grafana/explore-logs/pull/929
- Chore: Better type safety with ts-reset by @gtk-grafana in https://github.com/grafana/explore-logs/pull/926
- Queries: remove placeholder query and sanitize stream selector by @matyax in https://github.com/grafana/explore-logs/pull/930
- Field labels: histogram option for numeric fields by @gtk-grafana in https://github.com/grafana/explore-logs/pull/924
- LogsVolumePanel: Add infinite scroll for logs and display visible range by @matyax in https://github.com/grafana/explore-logs/pull/925
- Upgrade scenes to v5.29.0 by @gtk-grafana in https://github.com/grafana/explore-logs/pull/938
- Breakdown panels: Add shared crosshairs by @gtk-grafana in https://github.com/grafana/explore-logs/pull/940
- Logs Panel: Combine wrapLogMessage with prettifyLogMessage by @matyax in https://github.com/grafana/explore-logs/pull/944
- Value breakdowns: Update UI by @gtk-grafana in https://github.com/grafana/explore-logs/pull/936
- Remove go to explore button, add PanelMenu to logs & table panels by @gtk-grafana in https://github.com/grafana/explore-logs/pull/942
- Timeseries panels: Map field display names to color by @gtk-grafana in https://github.com/grafana/explore-logs/pull/937
- Panels: Keybindings by @gtk-grafana in https://github.com/grafana/explore-logs/pull/946
- chore: update livereload plugin port by @fcjack in https://github.com/grafana/explore-logs/pull/948
- fix(LogsVolumePanel): fix display of visible range when using cached data by @matyax in https://github.com/grafana/explore-logs/pull/955
- Line filter: add case sensitive line filter state to local storage by @gtk-grafana in https://github.com/grafana/explore-logs/pull/956
- Keybindings: support time range copy/paste by @gtk-grafana in https://github.com/grafana/explore-logs/pull/960
- Logs Volume: Set relative height and allow to collapse by @matyax in https://github.com/grafana/explore-logs/pull/964
- Logs Tab: Show log line count by @gtk-grafana in https://github.com/grafana/explore-logs/pull/951
- Logs panel: update service data when receiving new logs by @matyax in https://github.com/grafana/explore-logs/pull/967
- fix(panel-menu): menu throwing error in logs table by @svennergr in https://github.com/grafana/explore-logs/pull/968
- fix(panelmenu): `Investigations` causing multiple same keys by @svennergr in https://github.com/grafana/explore-logs/pull/965
- feat(patterns): use grafana's calculated `interval` as `step` by @svennergr in https://github.com/grafana/explore-logs/pull/974
- Table: Show log text not preserved in URL state by @gtk-grafana in https://github.com/grafana/explore-logs/pull/979
- Table: Column order not preserved in URL by @gtk-grafana in https://github.com/grafana/explore-logs/pull/978
- chore: run `yarn audit fix` by @gtk-grafana in https://github.com/grafana/explore-logs/pull/982
- Update `make docs` procedure by @github-actions in https://github.com/grafana/explore-logs/pull/972
- Add support to generate OTEL logs in generate script by @shantanualsi in https://github.com/grafana/explore-logs/pull/973
- Logs: Issue queries in forward or backward direction depending on the selected sorting option by @matyax in https://github.com/grafana/explore-logs/pull/970
- Breakdowns: Add share menu by @gtk-grafana in https://github.com/grafana/explore-logs/pull/983
- chore: clean up copy texts by @gtk-grafana in https://github.com/grafana/explore-logs/pull/987
- Logs panel: Direction and wrap URL state by @gtk-grafana in https://github.com/grafana/explore-logs/pull/985

## 1.0.4

- fix: console error when undefined jsondata.interval by @gtk-grafana in https://github.com/grafana/explore-logs/pull/877
- ServiceSelectionScene: Manual query runners by @gtk-grafana in https://github.com/grafana/explore-logs/pull/868
- Detected fields: Use detected_fields response to determine if avg_over_time query should be run by @gtk-grafana in https://github.com/grafana/explore-logs/pull/871
- feat(combineResponses): improve label comparison performance by @matyax in https://github.com/grafana/explore-logs/pull/880
- chore: bump @bsull/augurs to 0.6.0 by @sd2k in https://github.com/grafana/explore-logs/pull/882
- Labels variable: Combobox by @gtk-grafana in https://github.com/grafana/explore-logs/pull/878
- Chore: Rename the sorting option in explore metrics by @itsmylife in https://github.com/grafana/explore-logs/pull/883
- Go to Explore button: keep visual preferences in Explore link by @matyax in https://github.com/grafana/explore-logs/pull/885
- Service selection: Label selection UI by @gtk-grafana in https://github.com/grafana/explore-logs/pull/881
- Fix favoriting on label select by @gtk-grafana in https://github.com/grafana/explore-logs/pull/908
- Panel UI: Numeric filtering by @gtk-grafana in https://github.com/grafana/explore-logs/pull/894

## 1.0.3

- feat(exploration): add `grafana-lokiexplore-app/metric-exploration/v1` entrypoint by @svennergr in https://github.com/grafana/explore-logs/pull/840
- Initial label docs by @stevendungan in https://github.com/grafana/explore-logs/pull/853
- chore(intercept-banner): move into `container` by @svennergr in https://github.com/grafana/explore-logs/pull/854
- Logs panel: add button to copy link to log line by @matyax in https://github.com/grafana/explore-logs/pull/855
- fix: fix broken tsc-files command by @gtk-grafana in https://github.com/grafana/explore-logs/pull/860
- Add conditional extension point for testing sidecar functionality by @aocenas in https://github.com/grafana/explore-logs/pull/828
- Ad hoc variables: add support for detected_field/.../values by @gtk-grafana in https://github.com/grafana/explore-logs/pull/848
- Fix: tsc-files ignores tsconfig.json when called through husky hooks by @gtk-grafana in https://github.com/grafana/explore-logs/pull/867
- Config: Administrator config - max interval by @gtk-grafana in https://github.com/grafana/explore-logs/pull/843
- feat(shardSplitting): improve error handling by @matyax in https://github.com/grafana/explore-logs/pull/873

## 1.0.2

- Module: Split it up + heavy refactor by @gtk-grafana in https://github.com/grafana/explore-logs/pull/768
- Breakdowns: Remove service_name requirement by @gtk-grafana in https://github.com/grafana/explore-logs/pull/801
- docs: update installation instructions by @JStickler in https://github.com/grafana/explore-logs/pull/815
- Shard query splitting: use dynamic grouping by @matyax in https://github.com/grafana/explore-logs/pull/814
- fix(routing): check for sluggified value in URL by @matyax in https://github.com/grafana/explore-logs/pull/817
- Shard query splitting: add retrying flag to prevent cancelled requests by @matyax in https://github.com/grafana/explore-logs/pull/818
- Service selection: Showing incorrect list of services after changing datasource on breakdown views by @gtk-grafana in https://github.com/grafana/explore-logs/pull/811
- Service selection: Starting with labels besides service_name by @gtk-grafana in https://github.com/grafana/explore-logs/pull/813
- chore: upgrade grafana deps to 11.2.x and update extensions to use `addLink` by @svennergr in https://github.com/grafana/explore-logs/pull/824
- Patterns: Fix broken data link in pattern viz by @gtk-grafana in https://github.com/grafana/explore-logs/pull/831
- Shard query splitting: limit group size to be less than the remaining shards by @matyax in https://github.com/grafana/explore-logs/pull/829
- Patterns: fix flashing no patterns UI when loading by @gtk-grafana in https://github.com/grafana/explore-logs/pull/833
- Bundlewatch by @gtk-grafana in https://github.com/grafana/explore-logs/pull/830
- Bundlewatch: add main as base branch by @gtk-grafana in https://github.com/grafana/explore-logs/pull/836
- Primary label selection: Better empty volume UI by @gtk-grafana in https://github.com/grafana/explore-logs/pull/835
- Structured metadata: Refactor into new variable by @gtk-grafana in https://github.com/grafana/explore-logs/pull/826
- Breakdowns: Changing primary label doesn't update tab count by @gtk-grafana in https://github.com/grafana/explore-logs/pull/845
- Structured metadata: Changes to ad-hoc variable doesn't run detected_fields by @gtk-grafana in https://github.com/grafana/explore-logs/pull/849

## 1.0.0

- fix(shardQuerySplitting): do not emit empty data by @matyax in https://github.com/grafana/explore-logs/pull/793
- removed preview warning and updated some copy (added link to support) by @matryer in https://github.com/grafana/explore-logs/pull/792
- Frontend instrumentation by @gtk-grafana in https://github.com/grafana/explore-logs/pull/790
- Aggregated metrics: Use sum_over_time query for aggregated metric queries by @gtk-grafana in https://github.com/grafana/explore-logs/pull/789
- fix: fall back to mixed parser if the field is missing parser in url parameter by @gtk-grafana in https://github.com/grafana/explore-logs/pull/788
- Update workflows to use actions that don't need organization secrets by @svennergr in https://github.com/grafana/explore-logs/pull/784
- label values: fix label values stuck in loading state by @gtk-grafana in https://github.com/grafana/explore-logs/pull/783
- Shard query splitting: send the whole stream selector to fetch shard values by @gtk-grafana in https://github.com/grafana/explore-logs/pull/782
- chore(shardQuerySplitting): start in Streaming state by @BitDesert in https://github.com/grafana/explore-logs/pull/781
- fix(patterns-breakdown): fix expression to create pattern key breakdown by @gtk-grafana in https://github.com/grafana/explore-logs/pull/780
- fix(service-selection-scrolling): remove forced overflow scroll by @matyax in https://github.com/grafana/explore-logs/pull/779
- GA: remove preview badge by @gtk-grafana in https://github.com/grafana/explore-logs/pull/778
- GA: Remove preview copy in intercept banner by @gtk-grafana in https://github.com/grafana/explore-logs/pull/777

## 0.1.4

- Fields: include and exclude empty values by @gtk-grafana in https://github.com/grafana/explore-logs/pull/703
- Update `make docs` procedure by @github-actions in https://github.com/grafana/explore-logs/pull/716
- Displayed fields: persist selection in local storage and URL by @matyax in https://github.com/grafana/explore-logs/pull/733
- Sync loki versions in docker-compose.dev.yaml by @gtk-grafana in https://github.com/grafana/explore-logs/pull/745
- fix: grafana image tag by @BitDesert in https://github.com/grafana/explore-logs/pull/743
- generator: add new service with mix of json and logfmt by @gtk-grafana in https://github.com/grafana/explore-logs/pull/749
- Logs Volume Panel: properly handle "logs" detected level by @matyax in https://github.com/grafana/explore-logs/pull/751
- feat(detected-fields): use `/detected_fields` API by @svennergr in https://github.com/grafana/explore-logs/pull/736
- enable sharding in docker containers by @gtk-grafana in https://github.com/grafana/explore-logs/pull/754
- Line filter: Case sensitive search by @gtk-grafana in https://github.com/grafana/explore-logs/pull/744
- Shard query splitting: Split queries by stream shards by @matyax in https://github.com/grafana/explore-logs/pull/715
- chore: replace react-beautiful-dnd with successor by @gtk-grafana in https://github.com/grafana/explore-logs/pull/579
- Service selection: show previous filter text in service search input by @gtk-grafana in https://github.com/grafana/explore-logs/pull/763
- feat(generator): log `traceID` as structured metadata by @svennergr in https://github.com/grafana/explore-logs/pull/766
- Labels: Fix labels list not updating when detected_labels loads while user is viewing another tab by @gtk-grafana in https://github.com/grafana/explore-logs/pull/757
- Fields: Fix incorrect field count by @gtk-grafana in https://github.com/grafana/explore-logs/pull/761
- Link extensions: fix services with slash by @gtk-grafana in https://github.com/grafana/explore-logs/pull/770

## New Contributors

- @moxious made their first contribution in https://github.com/grafana/explore-logs/pull/673
- @github-actions made their first contribution in https://github.com/grafana/explore-logs/pull/716
- @BitDesert made their first contribution in https://github.com/grafana/explore-logs/pull/743

## 0.1.3

- added better hero image by @matryer in https://github.com/grafana/explore-logs/pull/598
- Updated plugin links to docs by @matryer in https://github.com/grafana/explore-logs/pull/599
- docs: Copyedit for style and docs standards by @JStickler in https://github.com/grafana/explore-logs/pull/582
- docs: embedded video by @matryer in https://github.com/grafana/explore-logs/pull/601
- docs: Fix heading levels by @JStickler in https://github.com/grafana/explore-logs/pull/602
- Docs update docs link by @matryer in https://github.com/grafana/explore-logs/pull/603
- docs: better sentence by @matryer in https://github.com/grafana/explore-logs/pull/604
- feat(log-context): add LogContext to logspanel by @svennergr in https://github.com/grafana/explore-logs/pull/607
- docs: more standardization edits by @JStickler in https://github.com/grafana/explore-logs/pull/605
- chore(main-release): bump patch version before doing a main build by @svennergr in https://github.com/grafana/explore-logs/pull/612
- docs: Update metadata with canonical URLs by @JStickler in https://github.com/grafana/explore-logs/pull/610
- Release 0.1.1 by @svennergr in https://github.com/grafana/explore-logs/pull/613
- chore: do not run release if triggered from drone by @svennergr in https://github.com/grafana/explore-logs/pull/615
- added a note about ephemeral patterns by @matryer in https://github.com/grafana/explore-logs/pull/619
- Value breakdowns: maintain filters between value changes by @matyax in https://github.com/grafana/explore-logs/pull/609
- Sorting: memoize sorting function by @matyax in https://github.com/grafana/explore-logs/pull/584
- Fields: fix loading forever when fields return empty by @gtk-grafana in https://github.com/grafana/explore-logs/pull/620
- Patterns: Show UI message when time range is too old to show patterns by @gtk-grafana in https://github.com/grafana/explore-logs/pull/618
- Chore: Clean up subscriptions by @gtk-grafana in https://github.com/grafana/explore-logs/pull/624
- Label queries: remove unneccessary filters and parsers in query expression by @svennergr in https://github.com/grafana/explore-logs/pull/628
- Service views: Prevent extra queries by @gtk-grafana in https://github.com/grafana/explore-logs/pull/629

## New Contributors

- @moxious made their first contribution in https://github.com/grafana/explore-logs/pull/673

## 0.1.2

- added better hero image by @matryer in https://github.com/grafana/explore-logs/pull/598
- Updated plugin links to docs by @matryer in https://github.com/grafana/explore-logs/pull/599
- docs: Copyedit for style and docs standards by @JStickler in https://github.com/grafana/explore-logs/pull/582
- docs: embedded video by @matryer in https://github.com/grafana/explore-logs/pull/601
- docs: Fix heading levels by @JStickler in https://github.com/grafana/explore-logs/pull/602
- Docs update docs link by @matryer in https://github.com/grafana/explore-logs/pull/603
- docs: better sentence by @matryer in https://github.com/grafana/explore-logs/pull/604
- feat(log-context): add LogContext to logspanel by @svennergr in https://github.com/grafana/explore-logs/pull/607
- docs: more standardization edits by @JStickler in https://github.com/grafana/explore-logs/pull/605
- chore(main-release): bump patch version before doing a main build by @svennergr in https://github.com/grafana/explore-logs/pull/612
- docs: Update metadata with canonical URLs by @JStickler in https://github.com/grafana/explore-logs/pull/610
- Release 0.1.1 by @svennergr in https://github.com/grafana/explore-logs/pull/613
- chore: do not run release if triggered from drone by @svennergr in https://github.com/grafana/explore-logs/pull/615
- added a note about ephemeral patterns by @matryer in https://github.com/grafana/explore-logs/pull/619
- Value breakdowns: maintain filters between value changes by @matyax in https://github.com/grafana/explore-logs/pull/609
- Sorting: memoize sorting function by @matyax in https://github.com/grafana/explore-logs/pull/584
- Fields: fix loading forever when fields return empty by @gtk-grafana in https://github.com/grafana/explore-logs/pull/620
- Patterns: Show UI message when time range is too old to show patterns by @gtk-grafana in https://github.com/grafana/explore-logs/pull/618
- Chore: Clean up subscriptions by @gtk-grafana in https://github.com/grafana/explore-logs/pull/624
- Label queries: remove unneccessary filters and parsers in query expression by @svennergr in https://github.com/grafana/explore-logs/pull/628
- Service views: Prevent extra queries by @gtk-grafana in https://github.com/grafana/explore-logs/pull/629

**Full Changelog**: https://github.com/grafana/explore-logs/compare/v0.1.1...v0.1.2

## 0.1.1

- feat(log-context): add LogContext to logspanel [#607](https://github.com/grafana/explore-logs/pull/607)

## 0.1.0

- Release public preview version.

> build
> node scripts/with-app-env.mjs vite build && npm run db:migrate

[nitro:vercel] ℹ Using nodejs22.x runtime.
[nitro:vercel] ℹ Using web entry format.
vite v8.3.2 building client environment for production...
transforming...
✓ 2898 modules transformed.
rendering chunks...
computing gzip size...
.vercel/output/static/assets/styles-BdxBAZsS.css              40.92 kB │ gzip:   8.28 kB
.vercel/output/static/assets/login-M06WjzG8.js                 1.65 kB │ gzip:   0.79 kB
.vercel/output/static/assets/cabinet-layout-DNhg4luT.js        1.70 kB │ gzip:   0.59 kB
.vercel/output/static/assets/schema-form-BX2zbrfZ.js           2.34 kB │ gzip:   0.99 kB
.vercel/output/static/assets/textarea-LGxdK7Xq.js              3.28 kB │ gzip:   1.32 kB
.vercel/output/static/assets/lazyRouteComponent-Fg6jF-9k.js    3.96 kB │ gzip:   1.45 kB
.vercel/output/static/assets/invite._token-CkIZ6TbF.js         4.02 kB │ gzip:   1.59 kB
.vercel/output/static/assets/new-ABgR2Gtu.js                   5.22 kB │ gzip:   2.07 kB
.vercel/output/static/assets/schema-CGPcdhYf.js                6.67 kB │ gzip:   2.14 kB
.vercel/output/static/assets/gates-kOX0QmDi.js                 7.41 kB │ gzip:   3.27 kB
.vercel/output/static/assets/useQuery-BcxBhHb0.js              8.01 kB │ gzip:   2.96 kB
.vercel/output/static/assets/react-DB-4Zxce.js                 8.52 kB │ gzip:   3.28 kB
.vercel/output/static/assets/routes-B_NHwvOL.js               10.17 kB │ gzip:   3.16 kB
.vercel/output/static/assets/link-CNDzMdj9.js                 11.93 kB │ gzip:   5.23 kB
.vercel/output/static/assets/dates-B00Vi_Q0.js                28.03 kB │ gzip:   8.06 kB
.vercel/output/static/assets/client-CzaTc0Rp.js               32.83 kB │ gzip:  12.38 kB
.vercel/output/static/assets/button-DHKhmumA.js               33.24 kB │ gzip:  11.01 kB
.vercel/output/static/assets/preload-helper-CicdFenT.js       43.86 kB │ gzip:  14.57 kB
.vercel/output/static/assets/_appId-CVzv_wWh.js               52.35 kB │ gzip:  17.21 kB
.vercel/output/static/assets/index-C0ZksYir.js               425.28 kB │ gzip: 130.36 kB

✓ built in 2.79s
vite v8.3.2 building ssr environment for production...
transforming...
✓ 339 modules transformed.
rendering chunks...
computing gzip size...
node_modules/.nitro/vite/services/ssr/assets/styles-BdxBAZsS.css                      40.92 kB │ gzip:  8.28 kB
node_modules/.nitro/vite/services/ssr/assets/kysely-adapter-Cj_QZw5p.js                0.05 kB │ gzip:  0.07 kB
node_modules/.nitro/vite/services/ssr/assets/start-5Z2QO8AU.js                         0.14 kB │ gzip:  0.13 kB
node_modules/.nitro/vite/services/ssr/assets/empty-plugin-adapters-D9UWiqvJ.js         0.22 kB │ gzip:  0.16 kB
node_modules/.nitro/vite/services/ssr/assets/utils-DX0sDq82.js                         0.78 kB │ gzip:  0.45 kB
node_modules/.nitro/vite/services/ssr/assets/dates-B0lpZguu.js                         1.34 kB │ gzip:  0.62 kB
node_modules/.nitro/vite/services/ssr/assets/textarea-BIV85Rvn.js                      1.36 kB │ gzip:  0.53 kB
node_modules/.nitro/vite/services/ssr/assets/middleware-BFcRe-bB.js                    1.91 kB │ gzip:  0.98 kB
node_modules/.nitro/vite/services/ssr/assets/isolation.server-CGNg1r0B.js              2.01 kB │ gzip:  1.05 kB
node_modules/.nitro/vite/services/ssr/assets/_tanstack-start-manifest_v-BWor_BtC.js    2.17 kB │ gzip:  0.65 kB
node_modules/.nitro/vite/services/ssr/assets/login-vAsiIsgs.js                         2.31 kB │ gzip:  0.98 kB
node_modules/.nitro/vite/services/ssr/assets/cabinet-layout-4MogEmMR.js                2.52 kB │ gzip:  0.79 kB
node_modules/.nitro/vite/services/ssr/assets/verify.server-CdaMc4Of.js                 3.50 kB │ gzip:  1.55 kB
node_modules/.nitro/vite/services/ssr/assets/schema-form-B00k9azm.js                   3.64 kB │ gzip:  1.18 kB
node_modules/.nitro/vite/services/ssr/assets/button-CZUCTCke.js                        4.32 kB │ gzip:  1.80 kB
node_modules/.nitro/vite/services/ssr/assets/invite._token-7mRLiMPV.js                 5.71 kB │ gzip:  1.87 kB
node_modules/.nitro/vite/services/ssr/assets/new-B639D-KG.js                           5.95 kB │ gzip:  1.94 kB
node_modules/.nitro/vite/services/ssr/assets/gates-DD1TsKoO.js                         7.28 kB │ gzip:  2.95 kB
node_modules/.nitro/vite/services/ssr/assets/schema-DTClIXAp.js                       13.23 kB │ gzip:  3.43 kB
node_modules/.nitro/vite/services/ssr/assets/db-FMNvmPvb.js                           13.52 kB │ gzip:  4.54 kB
node_modules/.nitro/vite/services/ssr/assets/routes-C2itUZ81.js                       14.01 kB │ gzip:  3.50 kB
node_modules/.nitro/vite/services/ssr/assets/router-BzKwN9S_.js                       15.57 kB │ gzip:  4.96 kB
node_modules/.nitro/vite/services/ssr/assets/url-BE6YaD7r.js                          15.82 kB │ gzip:  4.94 kB
node_modules/.nitro/vite/services/ssr/assets/directeur-CJbjJQCm.js                    15.85 kB │ gzip:  3.80 kB
node_modules/.nitro/vite/services/ssr/assets/_appId-BFVT13zQ.js                       26.88 kB │ gzip:  6.53 kB
node_modules/.nitro/vite/services/ssr/assets/client-1vAx-gM_.js                       37.99 kB │ gzip: 11.65 kB
node_modules/.nitro/vite/services/ssr/index.js                                        78.28 kB │ gzip: 20.14 kB
node_modules/.nitro/vite/services/ssr/assets/server-C2B3Zw-F.js                      345.16 kB │ gzip: 80.86 kB

✓ built in 1.20s

[nitro] ◐ Building [Nitro] (preset: vercel, compatibility: 2026-10-02)
[nitro] ✔ Generated public .vercel/output/static
vite v8.3.2 building nitro environment for production...
`output.codeSplitting.groups[0].name` is a function. Set `output.codeSplitting.groups[0].debugName` so the bundler timing report can identify this group.
transforming...
✓ 3355 modules transformed.
ℹ Tracing dependencies:
- tslib (2.8.1)
✔ Traced 1 dependencies (4 files) in 66ms.
ℹ Ensure your production environment matches the builder OS and architecture (linux-x64) to avoid native module issues.
rendering chunks...
computing gzip size...
.vercel/output/functions/__server.func/_ssr/start-5Z2QO8AU.mjs                         0.14 kB │ gzip:   0.13 kB
.vercel/output/functions/__server.func/_ssr/kysely-adapter-Cj_QZw5p.mjs                0.15 kB │ gzip:   0.12 kB
.vercel/output/functions/__server.func/_ssr/empty-plugin-adapters-D9UWiqvJ.mjs         0.23 kB │ gzip:   0.16 kB
.vercel/output/functions/__server.func/_chunks/core.mjs                                0.25 kB │ gzip:   0.18 kB
.vercel/output/functions/__server.func/_libs/zod.mjs                                   0.36 kB │ gzip:   0.22 kB
.vercel/output/functions/__server.func/_ssr/utils-DX0sDq82.mjs                         0.88 kB │ gzip:   0.52 kB
.vercel/output/functions/__server.func/_chunks/ssr-renderer.mjs                        0.96 kB │ gzip:   0.49 kB
.vercel/output/functions/__server.func/_libs/defu.mjs                                  1.41 kB │ gzip:   0.58 kB
.vercel/output/functions/__server.func/_ssr/dates-B0lpZguu.mjs                         1.49 kB │ gzip:   0.66 kB
.vercel/output/functions/__server.func/_ssr/textarea-BIV85Rvn.mjs                      1.64 kB │ gzip:   0.63 kB
.vercel/output/functions/__server.func/_libs/radix-ui__primitive.mjs                   1.83 kB │ gzip:   0.72 kB
.vercel/output/functions/__server.func/_runtime.mjs                                    1.92 kB │ gzip:   0.87 kB
.vercel/output/functions/__server.func/_ssr/middleware-BFcRe-bB.mjs                    1.97 kB │ gzip:   1.01 kB
.vercel/output/functions/__server.func/_ssr/isolation.server-CGNg1r0B.mjs              2.05 kB │ gzip:   1.08 kB
.vercel/output/functions/__server.func/_tanstack-start-manifest_v-BWor_BtC.mjs         2.22 kB │ gzip:   0.68 kB
.vercel/output/functions/__server.func/_ssr/login-vAsiIsgs.mjs                         2.79 kB │ gzip:   1.06 kB
.vercel/output/functions/__server.func/_libs/class-variance-authority+clsx.mjs         3.17 kB │ gzip:   1.24 kB
.vercel/output/functions/__server.func/_ssr/cabinet-layout-4MogEmMR.mjs                3.17 kB │ gzip:   0.88 kB
.vercel/output/functions/__server.func/_ssr/verify.server-CdaMc4Of.mjs                 3.54 kB │ gzip:   1.58 kB
.vercel/output/functions/__server.func/_libs/better-auth__utils.mjs                    3.80 kB │ gzip:   1.31 kB
.vercel/output/functions/__server.func/_ssr/schema-form-B00k9azm.mjs                   4.32 kB │ gzip:   1.31 kB
.vercel/output/functions/__server.func/_ssr/button-CZUCTCke.mjs                        4.69 kB │ gzip:   1.93 kB
.vercel/output/functions/__server.func/_libs/radix-ui__react-context+react.mjs         5.74 kB │ gzip:   1.67 kB
.vercel/output/functions/__server.func/_libs/nanostores.mjs                            6.11 kB │ gzip:   1.98 kB
.vercel/output/functions/__server.func/_ssr/invite._token-7mRLiMPV.mjs                 6.76 kB │ gzip:   1.96 kB
.vercel/output/functions/__server.func/_ssr/new-B639D-KG.mjs                           6.99 kB │ gzip:   2.09 kB
.vercel/output/functions/__server.func/_ssr/gates-DD1TsKoO.mjs                         7.70 kB │ gzip:   3.07 kB
.vercel/output/functions/__server.func/_libs/lucide-react.mjs                         11.45 kB │ gzip:   2.86 kB
.vercel/output/functions/__server.func/_libs/tanstack__history.mjs                    12.50 kB │ gzip:   3.70 kB
.vercel/output/functions/__server.func/_ssr/schema-DTClIXAp.mjs                       13.28 kB │ gzip:   3.46 kB
.vercel/output/functions/__server.func/_ssr/db-FMNvmPvb.mjs                           13.47 kB │ gzip:   4.57 kB
.vercel/output/functions/__server.func/_libs/better-auth__memory-adapter.mjs          14.71 kB │ gzip:   4.12 kB
.vercel/output/functions/__server.func/_libs/tanstack__react-query.mjs                14.75 kB │ gzip:   4.11 kB
.vercel/output/functions/__server.func/_ssr/url-BE6YaD7r.mjs                          15.54 kB │ gzip:   4.93 kB
.vercel/output/functions/__server.func/_ssr/router-BzKwN9S_.mjs                       15.78 kB │ gzip:   5.04 kB
.vercel/output/functions/__server.func/_ssr/directeur-CJbjJQCm.mjs                    15.83 kB │ gzip:   3.84 kB
.vercel/output/functions/__server.func/_ssr/routes-C2itUZ81.mjs                       16.89 kB │ gzip:   3.64 kB
.vercel/output/functions/__server.func/_libs/@better-auth/telemetry+[...].mjs         17.53 kB │ gzip:   4.90 kB
.vercel/output/functions/__server.func/_libs/h3-v2+rou3.mjs                           17.58 kB │ gzip:   5.16 kB
.vercel/output/functions/__server.func/_libs/@radix-ui/react-compose-refs+[...].mjs   17.61 kB │ gzip:   4.83 kB
.vercel/output/functions/__server.func/_libs/h3+rou3+srvx.mjs                         22.57 kB │ gzip:   6.12 kB
.vercel/output/functions/__server.func/_libs/noble__hashes.mjs                        23.93 kB │ gzip:   7.95 kB
.vercel/output/functions/__server.func/_libs/@tanstack/router-core+[...].mjs          29.60 kB │ gzip:   7.98 kB
.vercel/output/functions/__server.func/_appId-BFVT13zQ.mjs                            31.34 kB │ gzip:   6.75 kB
.vercel/output/functions/__server.func/index.mjs                                      32.24 kB │ gzip:  10.02 kB
.vercel/output/functions/__server.func/_ssr/client-1vAx-gM_.mjs                       37.30 kB │ gzip:  11.71 kB
.vercel/output/functions/__server.func/_libs/jose.mjs                                 38.65 kB │ gzip:   8.59 kB
.vercel/output/functions/__server.func/_libs/noble__ciphers.mjs                       47.40 kB │ gzip:  14.67 kB
.vercel/output/functions/__server.func/_libs/sonner.mjs                               53.69 kB │ gzip:  12.12 kB
.vercel/output/functions/__server.func/_ssr/ssr.mjs                                   76.57 kB │ gzip:  20.08 kB
.vercel/output/functions/__server.func/_libs/@radix-ui/react-dialog+[...].mjs         87.25 kB │ gzip:  20.43 kB
.vercel/output/functions/__server.func/_libs/tailwind-merge.mjs                       88.92 kB │ gzip:  15.71 kB
.vercel/output/functions/__server.func/_libs/date-fns.mjs                            105.18 kB │ gzip:  20.08 kB
.vercel/output/functions/__server.func/_libs/tanstack__query-core.mjs                112.86 kB │ gzip:  26.53 kB
.vercel/output/functions/__server.func/_libs/pg.mjs                                  150.17 kB │ gzip:  34.88 kB
.vercel/output/functions/__server.func/_ssr/server-C2B3Zw-F.mjs                      339.50 kB │ gzip:  80.22 kB
.vercel/output/functions/__server.func/_libs/@better-auth/kysely-adapter+[...].mjs   473.01 kB │ gzip:  78.51 kB
.vercel/output/functions/__server.func/_libs/electric-sql__pglite.mjs                751.95 kB │ gzip: 153.28 kB
.vercel/output/functions/__server.func/_libs/@tanstack/react-router+[...].mjs        793.40 kB │ gzip: 166.74 kB
.vercel/output/functions/__server.func/_libs/@better-auth/core+[...].mjs             809.79 kB │ gzip: 160.36 kB

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/index.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/index.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/useMatch.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/useMatch.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/utils.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/utils.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/useNavigate.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/useNavigate.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/CatchBoundary.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/CatchBoundary.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/ClientOnly.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/ClientOnly.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/useRouter.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/useRouter.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/link.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/link.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/useBlocker.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/useBlocker.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/RouterProvider.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/RouterProvider.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/useRouterState.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/useRouterState.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/Matches.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/Matches.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/Match.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/Match.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/useLocation.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/useLocation.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/Asset.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/Asset.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/HeadContent.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/HeadContent.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/matchContext.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/matchContext.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/nonRouteComponentContext.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/nonRouteComponentContext.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/routerContext.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/routerContext.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-router/dist/esm/Transitioner.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-router/dist/esm/Transitioner.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/sonner/dist/index.mjs" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/sonner/dist/index.mjs:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m 'use client';
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-query/build/modern/useQueries.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-query/build/modern/useQueries.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-query/build/modern/IsRestoringProvider.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-query/build/modern/IsRestoringProvider.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-query/build/modern/QueryErrorResetBoundary.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-query/build/modern/QueryErrorResetBoundary.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-query/build/modern/useSuspenseQuery.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-query/build/modern/useSuspenseQuery.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-query/build/modern/useQuery.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-query/build/modern/useQuery.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECTIVE] [0mThe semantics of the module level directive "use client" in "node_modules/@tanstack/react-query/build/modern/useSuspenseInfiniteQuery.js" may not be preserved when bundling.
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m node_modules/@tanstack/react-query/build/modern/useSuspenseInfiniteQuery.js:1:1 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m1 │[0m "use client";
 [38;5;240m  │[0m ──────┬──────  
 [38;5;240m  │[0m       ╰──────── module level directive may not be preserved
 [38;5;240m  │[0m 
 [38;5;240m  │[0m [38;5;115mHelp[0m: For more information, see https://rolldown.rs/in-depth/directives#other-directives
[38;5;246m───╯[0m

[33m[MODULE_LEVEL_DIRECT
[output truncated to 32768 bytes shown; read /tmp/sessions/1d0f95a0-e4e7-4be1-a3d7-61480edb8cc0/terminal/01a0fa08-9a2f-7d63-b61d-4a78b6acf2c1.log for the full output]

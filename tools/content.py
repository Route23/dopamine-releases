# -*- coding: utf-8 -*-
"""配布サイトの文言の正典（#513）。**日英をここで 1 か所に持つ。**

`python3 tools/gen.py` が index.html と assets/i18n.js を書き出す。
HTML は英語だけで完結し（JS 無効でも読める）、i18n.js が ja に差し替える。
"""

# (key, en, ja)
UI = [
    ("tagline", "A browser, a terminal, a file manager and a code editor in one macOS window. Split it into panes, keep everything on screen, and stop switching apps.",
                "ブラウザ、ターミナル、ファイルマネージャー、コードエディタを 1 つの macOS の窓に。ペインに割って全部を並べておけば、もうアプリを行き来しなくていい。"),
    ("slogan.sub", "Everything you work with, side by side, in one window.", "仕事の道具を全部、1 つの窓に並べて。"),
    ("spec", "Apple Silicon · macOS 14+ · 33 themes · 12 languages · no account",
             "Apple Silicon · macOS 14 以降 · テーマ 33 種 · 12 言語 · アカウント不要"),
    ("download", "Download for macOS", "macOS 版をダウンロード"),
    ("degraded", "Couldn’t load release details from GitHub right now — the download link above still works.",
                 "GitHub からリリースの情報を読めませんでした。上のダウンロードボタンはそのまま使えます。"),
    ("screens.lead", "Every picture below is the app as it ships — no mock-ups.",
                     "下の絵はすべて、配っているアプリそのままの画面です。"),
    ("features.lead", "Everything dopamine does, in one table.", "dopamine にできることの全部を 1 枚の表に。"),
    ("th.no", "N°", "N°"),
    ("th.area", "Area", "面"),
    ("th.what", "What it does", "できること"),
    ("legend", "● = built in, no extension needed    N° = section", "● = 最初から入っている（拡張は要らない）    N° = 区分"),
    ("install.brew", "Install with Homebrew", "Homebrew で入れる"),
    ("install.brew.note", "The cask clears the quarantine flag for you.", "cask が隔離フラグを外してくれます。"),
    ("install.dmg", "First launch from the .dmg", ".dmg から初めて開くとき"),
    ("install.dmg.body", "dopamine is signed ad-hoc and not notarized by Apple, so macOS refuses to open it the first time. Run this once, then open the app:",
                         "dopamine は ad-hoc 署名で、Apple の公証を受けていません。そのため macOS は最初の 1 回だけ開くのを断ります。次を 1 度だけ実行してから開いてください。"),
    ("install.req", "Requirements", "必要なもの"),
    ("req.os", "macOS 14 (Sonoma) or later", "macOS 14（Sonoma）以降"),
    ("req.cpu", "Apple Silicon (arm64) only — there is no Intel build", "Apple Silicon（arm64）のみ。Intel 版はありません"),
    ("updates", "Updates arrive inside the app and are signed with ed25519.", "アップデートはアプリの中から届き、ed25519 で署名されています。"),
    ("copy", "Copy", "コピー"),
    ("copied", "Copied", "コピーしました"),
    ("footer.releases", "All releases", "すべてのリリース"),
    ("footer.bug", "Report a bug", "不具合を報告"),
    ("footer.github", "GitHub", "GitHub"),
    ("made", "Made on a Mac · distributed free", "Mac で作って、無料で配っています"),
    # app.js が使う文言
    ("dl.latest", "Download dopamine {tag}", "dopamine {tag} をダウンロード"),
    ("dl.none", "No public build yet", "まだ公開版はありません"),
    ("dl.first", "The first release will be v0.1.0.", "最初のリリースは v0.1.0 です。"),
    ("dl.latestOnly", "Latest release: {tag}", "最新のリリース: {tag}"),
    ("rel.title", "Releases", "リリース"),
    ("rel.lead", "Every build, newest first. macOS 14+, Apple Silicon.", "すべての版を新しい順に。macOS 14 以降・Apple Silicon。"),
    ("rel.none", "No releases yet. The first public build will be v0.1.0.", "まだリリースはありません。最初の公開版は v0.1.0 です。"),
    ("rel.fail", "Couldn’t load the release list from GitHub right now.", "GitHub からリリースの一覧を読めませんでした。"),
    ("rel.onGithub", "See all releases on GitHub", "GitHub ですべてのリリースを見る"),
    ("rel.pre", "pre-release", "プレリリース"),
    ("home", "Home", "ホーム"),
]

# 見出し: (key, 日本語, 英語) —— **両方いつも出す**（Rhodia の「LA GAMME - THE SELECTION」）
HEADS = [
    ("h.screens", "画面", "Screens"),
    ("h.features", "機能", "Features"),
    ("h.install", "導入", "Install"),
    ("h.themes", "テーマ", "Themes"),
]

# スクショ: (file, en caption, ja caption, big?)
SHOTS = [
    ("workspace", "One window, no switching: the file tree, a web page, a terminal, the editor with git marks and a Run lens, and Files.",
                  "窓は 1 つ、行き来はゼロ。ファイルツリー、Web ページ、ターミナル、git の印と Run のレンズが付いたエディタ、Files。", True),
    ("source-control", "Source control in the sidebar: staged and unstaged changes, a commit box, and the branch graph — next to the terminal’s git log.",
                       "サイドバーのソース管理。ステージ済みと未ステージの変更、コミット欄、枝のグラフ。横のターミナルには git log。", False),
    ("diff", "Diff pane, side by side: the file’s line numbers, word-level changes, and unchanged lines folded away.",
             "差分ペイン。左右に並べ、ファイルの行番号と語単位の差を出し、変わっていない行は畳む。", False),
    ("files-rss", "The file tree, Files in gallery view, and an RSS pane reading two feeds.", "ファイルツリー、ギャラリー表示の Files、2 つのフィードを読む RSS ペイン。", False),
    ("settings-themes", "Settings live in their own window. 33 themes, picked from pictures.", "設定は別の窓。テーマ 33 種を絵から選ぶ。", False),
    ("settings-editor", "Every setting is a card with its settings.json key and a live sample.", "設定は 1 つずつカードで、settings.json の鍵と実寸の見本付き。", False),
    ("settings-filter", "Filter across every section; pictures instead of dropdowns.", "全区分をまたいで絞り込み。選択肢は絵で選ぶ。", False),
]
THEME_SHOTS = [
    ("theme-catppuccin-mocha", "Catppuccin Mocha"),
    ("theme-everforest-dark", "Everforest Dark"),
    ("theme-monokai-pro", "Monokai Pro"),
    ("theme-solarized-light", "Solarized Light"),
]

# 機能の全量: (en area, ja area, [(en, ja), ...])
FEATURES = [
    ("Panes & Spaces", "ペインとスペース", [
        ("Split any area into panes: browser, terminal, files, editor, RSS", "どこでもペインに割れる。ブラウザ・ターミナル・Files・エディタ・RSS"),
        ("Several Spaces, switched with ⌘1–⌘8", "スペースを何枚も持てて、⌘1〜⌘8 で切り替え"),
        ("Group + Tab mode with nested groups, like VS Code", "VS Code のような入れ子のグループ＋タブのモード"),
        ("Drag tabs to reorder, or drop them on an edge to split", "タブはドラッグで並べ替え、端に落とせば分割"),
        ("Tile view, or Strip view that pages through panes", "タイル表示と、ペインを 1 枚ずつめくるストリップ表示"),
        ("Mission Control overview with live thumbnails (⌃↑)", "縮図が生きている Mission Control（⌃↑）"),
        ("SpaceTree: every Space and pane in the sidebar, renamed in place", "SpaceTree：全スペースとペインをサイドバーに並べ、その場で名前を変える"),
        ("Pane headers with 8 colours and a memory readout", "8 色から選べるペインヘッダーと、ペインごとのメモリ表示"),
        ("Session restore: Spaces, panes, names and zoom come back", "セッションの復元。スペース・ペイン・名前・倍率が戻る"),
        ("Reopen closed panes (⇧⌘T), duplicate panes, Zen Mode (⌃⌘Z)", "閉じたペインを戻す（⇧⌘T）・複製・Zen モード（⌃⌘Z）"),
    ]),
    ("Browser", "ブラウザ", [
        ("WebKit browsing with a search screen, suggestions and history", "WebKit のブラウザ。検索画面・サジェスト・履歴"),
        ("Built-in ad blocking with per-site exceptions", "広告ブロックが最初から入っていて、サイトごとに外せる"),
        ("Secret Mode (⇧⌘N): nothing written to disk", "シークレットモード（⇧⌘N）：ディスクに何も残さない"),
        ("Translate a page into 12 languages, and back", "ページを 12 言語に翻訳して、元にも戻せる"),
        ("Page zoom remembered per site; find in page (⌘F)", "サイトごとに覚える倍率・ページ内検索（⌘F）"),
        ("Native right-click menu: save, print, share, view source", "ネイティブの右クリックメニュー：保存・印刷・共有・ソース表示"),
        ("Full history window (⌘Y), downloads, clear browsing data", "全履歴の窓（⌘Y）・ダウンロード・閲覧データの消去"),
        ("Proxy setting; open links in your default browser", "プロキシの設定・既定のブラウザで開く"),
    ]),
    ("Terminal", "ターミナル", [
        ("Fast terminal built on ghostty-web, 33 colour schemes", "ghostty-web の速いターミナル。配色 33 種"),
        ("⌘-click paths and URLs to open them in the editor or browser", "パスや URL を ⌘ クリックでエディタやブラウザに開く"),
        ("Shell profiles, “Open in Terminal”, venv auto-activation", "シェルのプロファイル・「ターミナルで開く」・venv の自動有効化"),
        ("Shell integration (OSC 133 / OSC 7), exit codes shown", "シェル統合（OSC 133 / OSC 7）と終了コードの表示"),
        ("Asks before closing a shell that is still running", "動いているシェルを閉じる前に確認"),
        ("Spots localhost ports in output and can open them", "出力の localhost のポートを見つけて開ける"),
        ("⌃V literal insert reaches the shell", "⌃V のリテラル挿入がシェルに届く"),
    ]),
    ("Files", "Files", [
        ("Finder-style browser: list, icon, column and gallery views", "Finder のような 4 つの表示：リスト・アイコン・カラム・ギャラリー"),
        ("9 list columns, Finder-style sorting, inline folder expansion", "9 つの列・Finder と同じ並び順・その場でフォルダーを開く"),
        ("Get Info with Finder tags; filter by tag", "Finder タグを編集できる情報パネルとタグの絞り込み"),
        ("Image lightbox and slideshow", "画像のライトボックスとスライドショー"),
        ("Cut, copy and paste between panes; drag to Finder or the web", "ペイン間の切り取り・コピー・貼り付け、Finder や Web へのドラッグ"),
        ("“Replace or keep both?” when names clash; inline rename", "同名のときは「置き換える / 両方残す」、その場で名前変更"),
    ]),
    ("Editor", "エディタ", [
        ("Code editor with tree-sitter highlighting, one file per pane", "tree-sitter で色付けするコードエディタ。1 ペイン 1 ファイル"),
        ("Sidebar file tree with several roots", "複数の根を持てるサイドバーのファイルツリー"),
        ("Find and replace with smartcase, whole word and regex", "smartcase・単語・正規表現の検索と置換"),
        ("Minimap with the caret’s line and MARK: / #region headers", "キャレット行と MARK: / #region の見出しが出るミニマップ"),
        ("Sticky scroll, scrollbar markers, breadcrumbs", "追従スクロール・スクロールバーの印・階層リンク"),
        ("Bracket colours, guides, folding, rulers, visible whitespace", "括弧の色・ガイド・折りたたみ・ルーラー・空白の表示"),
        ("Keeps indentation, encoding and line endings as found", "字下げ・文字コード・改行コードを見つけたまま保つ"),
        ("Format on save, type or paste; auto save", "保存時・入力時・貼り付け時の整形と自動保存"),
        ("Local history and a timeline of every save", "ローカル履歴と、保存ごとのタイムライン"),
        ("Unsaved drafts survive quitting", "保存していない書きかけは終了しても残る"),
    ]),
    ("Language servers", "言語サーバ", [
        ("Diagnostics as squiggles and at the end of the line", "波線と行末に出る診断"),
        ("Completion, hover, parameter hints, inlay hints", "補完・ホバー・引数のヒント・インレイヒント"),
        ("Go to definition (⌃⌘J), code actions, semantic colours", "定義へ移動（⌃⌘J）・コードアクション・意味づけの色"),
        ("CodeLens, with Run and Test for Rust; lists references", "CodeLens。Rust は Run と Test、参照は一覧から選べる"),
        ("Problems (⇧⌘M) and Output (⇧⌘U) panes", "問題ペイン（⇧⌘M）と出力ペイン（⇧⌘U）"),
        ("Asks before trusting a folder; trust can be revoked", "フォルダーを信頼する前に確認し、あとで取り消せる"),
    ]),
    ("Git", "Git", [
        ("Source control: Changes and Graph sections", "ソース管理：変更とグラフ"),
        ("Commit, stash, pull, push, fetch, branches, create PR", "コミット・stash・pull・push・fetch・ブランチ・PR 作成"),
        ("Change marks in the gutter; revert or stage one hunk", "ガターの変更の印。塊 1 つだけ戻す / ステージする"),
        ("Inline blame at the end of the caret’s line", "キャレット行の末尾に blame"),
        ("Diff pane: side by side or inline, with line numbers", "差分ペイン：左右か重ねて、行番号付き"),
    ]),
    ("Search & Tasks", "検索とタスク", [
        ("Search in Files across the workspace with replace preview (⇧⌘F)", "ワークスペース全体の検索と置換のプレビュー（⇧⌘F）"),
        ("Run Task… finds npm, pnpm, yarn, bun, Cargo and Make targets", "「タスクを実行…」が npm / pnpm / yarn / bun / Cargo / Make を見つける"),
        ("Pulls problems out of task output ($rustc, $tsc, $eslint, $gcc)", "タスクの出力から問題を拾う（$rustc・$tsc・$eslint・$gcc）"),
        ("Sound and announcement signals for tasks and saves", "タスクや保存を音と読み上げで知らせる"),
    ]),
    ("Appearance", "外観", [
        ("33 themes: Ayu, Gruvbox, One, Catppuccin, Monokai, Everforest, Iceberg, Solarized", "テーマ 33 種：Ayu・Gruvbox・One・Catppuccin・Monokai・Everforest・Iceberg・Solarized"),
        ("Follows macOS light and dark, with a theme for each", "macOS の明暗に追従し、明暗それぞれのテーマを選べる"),
        ("Wallpaper and per-area translucency", "壁紙と、場所ごとの透過"),
        ("UI font, size and density; Reduce Motion and Transparency", "UI の字・大きさ・密度、動きと透過を減らす"),
        ("UI in 12 languages, switched without restarting", "12 言語の UI。再起動せずに切り替え"),
    ]),
    ("Keyboard", "キーボード", [
        ("Full native menu bar with standard macOS shortcuts", "macOS 標準のショートカットが効くネイティブのメニューバー"),
        ("Record your own keybindings", "キーの割り当てを自分で録る"),
        ("Keystroke visualiser for screen recordings", "画面収録向けのキー入力の表示"),
        ("Focus follows the mouse (optional)", "マウスでフォーカス（選べる）"),
    ]),
    ("RSS & Profiles", "RSS とプロファイル", [
        ("RSS pane with feed chips and thumbnails; articles open in a pane", "フィードのチップとサムネイルの RSS ペイン。記事はペインで開く"),
        ("Separate browsing profiles, each with an avatar and colour", "アバターと色を持てる別々のプロファイル"),
        ("Bookmark tree with drag and drop; bookmark all panes", "ドラッグで並べるブックマークの木。全ペインをまとめて登録"),
    ]),
    ("Integrations", "連携", [
        ("Spotify widget in the footer: now playing and controls", "フッターの Spotify：再生中の曲と操作"),
        ("Discord Rich Presence that shares only the pane type", "Discord のリッチプレゼンス。出すのはペインの種類だけ"),
    ]),
    ("Privacy & Updates", "プライバシーと更新", [
        ("Every URL is checked before it loads", "読み込む前にすべての URL を検める"),
        ("Crash log stays on your Mac, never sent", "クラッシュログは Mac の中だけ。送らない"),
        ("In-app updates, signed with ed25519; one click to swap and relaunch", "アプリ内の更新。ed25519 の署名付きで、1 クリックで入れ替えて再起動"),
        ("Launches in about 0.9 s with ad blocking on", "広告ブロックを入れたまま約 0.9 秒で起動"),
    ]),
    ("Settings", "設定", [
        ("Settings in their own window (⌘,), one card per setting", "設定は別の窓（⌘,）。1 つの設定に 1 枚のカード"),
        ("Right-click any area of the UI to open its settings", "UI のどこでも右クリックでその場所の設定へ"),
        ("Filter across sections; options chosen from pictures", "区分をまたいで絞り込み、選択肢は絵で選ぶ"),
        ("Each card shows its settings.json key and default", "カードごとに settings.json の鍵と既定値を表示"),
        ("Keep settings.json in iCloud or Dropbox; live reload", "settings.json を iCloud や Dropbox に置けて、書き換えは即反映"),
    ]),
]

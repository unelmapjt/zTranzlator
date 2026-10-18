"""
zTranzlator - Internationalization (i18n) & Multi-Language Support
アプリUI表示言語: 日本語(ja), English(en), 한국어(ko), 简体中文(zh-CN), Español(es)
MOD翻訳先言語: JP, KO, CN, CH, ES, RU, FR, DE, PL, PTBR, IT 等
"""

SUPPORTED_UI_LANGUAGES = {
    "ja": "日本語 (Japanese)",
    "en": "English",
    "ko": "한국어 (Korean)",
    "zh-CN": "简体中文 (Simplified Chinese)",
    "es": "Español (Spanish)",
}

SUPPORTED_TARGET_LANGUAGES = {
    "JP": {"name": "日本語", "en_name": "Japanese", "suffix": "_JA"},
    "KO": {"name": "한국어", "en_name": "Korean", "suffix": "_KO"},
    "CN": {"name": "简体中文", "en_name": "Simplified Chinese", "suffix": "_CN"},
    "CH": {"name": "繁體中文", "en_name": "Traditional Chinese", "suffix": "_CH"},
    "ES": {"name": "Español", "en_name": "Spanish", "suffix": "_ES"},
    "RU": {"name": "Русский", "en_name": "Russian", "suffix": "_RU"},
    "FR": {"name": "Français", "en_name": "French", "suffix": "_FR"},
    "DE": {"name": "Deutsch", "en_name": "German", "suffix": "_DE"},
    "PL": {"name": "Polski", "en_name": "Polish", "suffix": "_PL"},
    "PTBR": {"name": "Português (Brasil)", "en_name": "Brazilian Portuguese", "suffix": "_PTBR"},
    "IT": {"name": "Italiano", "en_name": "Italian", "suffix": "_IT"},
}

STRINGS = {
    "app_title": {
        "ja": "zTranzlator — Project Zomboid Build 42 総合翻訳スイート",
        "en": "zTranzlator — Project Zomboid Build 42 Translation Suite",
        "ko": "zTranzlator — Project Zomboid Build 42 종합 번역 도구",
        "zh-CN": "zTranzlator — 僵尸毁灭工程 Build 42 综合翻译套件",
        "es": "zTranzlator — Suite de Traducción para Project Zomboid Build 42",
    },
    "btn_settings": {
        "ja": "⚙ 翻訳設定",
        "en": "⚙ Settings",
        "ko": "⚙ 번역 설정",
        "zh-CN": "⚙ 翻译设置",
        "es": "⚙ Ajustes",
    },
    "btn_manual": {
        "ja": "マニュアル (HTML)",
        "en": "Manual (HTML)",
        "ko": "매뉴얼 (HTML)",
        "zh-CN": "使用说明 (HTML)",
        "es": "Manual (HTML)",
    },
    "btn_import_zip": {
        "ja": "ZIPインポート",
        "en": "Import ZIP",
        "ko": "ZIP 가져오기",
        "zh-CN": "导入 ZIP",
        "es": "Importar ZIP",
    },
    "btn_rescan": {
        "ja": "再スキャン",
        "en": "Rescan",
        "ko": "다시 스캔",
        "zh-CN": "重新扫描",
        "es": "Reescanear",
    },
    "search_placeholder": {
        "ja": "MODを検索...",
        "en": "Search MODs...",
        "ko": "모드 검색...",
        "zh-CN": "搜索 MOD...",
        "es": "Buscar MODs...",
    },
    "col_mod_name": {
        "ja": "MOD名",
        "en": "Mod Name",
        "ko": "모드 이름",
        "zh-CN": "MOD名称",
        "es": "Nombre del MOD",
    },
    "col_progress": {
        "ja": "翻訳率",
        "en": "Progress",
        "ko": "진행률",
        "zh-CN": "进度",
        "es": "Progreso",
    },
    "col_id": {
        "ja": "ID",
        "en": "ID",
        "ko": "ID",
        "zh-CN": "ID",
        "es": "ID",
    },
    "col_en": {
        "ja": "原文 (English)",
        "en": "Original (English)",
        "ko": "원문 (English)",
        "zh-CN": "原文 (English)",
        "es": "Original (English)",
    },
    "col_trans": {
        "ja": "訳文 ({lang})",
        "en": "Translation ({lang})",
        "ko": "번역 ({lang})",
        "zh-CN": "译文 ({lang})",
        "es": "Traducción ({lang})",
    },
    "col_arch": {
        "ja": "根拠",
        "en": "Source",
        "ko": "근거",
        "zh-CN": "来源",
        "es": "Fuente",
    },
    "col_status": {
        "ja": "ステータス",
        "en": "Status",
        "ko": "상태",
        "zh-CN": "状态",
        "es": "Estado",
    },
    "col_file": {
        "ja": "出現ファイル",
        "en": "Source File",
        "ko": "발견된 파일",
        "zh-CN": "来源文件",
        "es": "Archivo de Origen",
    },
    "grid_search_placeholder": {
        "ja": "🔍 原文・訳文・タイプ・ファイルで絞り込み...",
        "en": "🔍 Filter by Original, Translation, Type, File...",
        "ko": "🔍 원문・번역・타입・파일로 검색...",
        "zh-CN": "🔍 按原文、译文、类型、文件筛选...",
        "es": "🔍 Filtrar por original, traducción, tipo, archivo...",
    },
    "btn_clear": {
        "ja": "✕ クリア",
        "en": "✕ Clear",
        "ko": "✕ 지우기",
        "zh-CN": "✕ 清除",
        "es": "✕ Limpiar",
    },
    "filter_all": {
        "ja": "すべて表示",
        "en": "Show All",
        "ko": "전체 표시",
        "zh-CN": "全部显示",
        "es": "Mostrar Todo",
    },
    "btn_translate_dict": {
        "ja": "一括辞書翻訳を実行 (内蔵)",
        "en": "Run Batch Dictionary Translation",
        "ko": "일괄 사전 번역 실행 (내장)",
        "zh-CN": "执行批量词典翻译 (内建)",
        "es": "Ejecutar Traducción de Diccionario",
    },
    "btn_translate_gemini": {
        "ja": "一括AI翻訳を実行 (Gemini)",
        "en": "Run Batch AI Translation (Gemini)",
        "ko": "일괄 AI 번역 실행 (Gemini)",
        "zh-CN": "执行批量AI翻译 (Gemini)",
        "es": "Ejecutar Traducción AI (Gemini)",
    },
    "btn_translate_openai": {
        "ja": "一括AI翻訳を実行 (クラウド)",
        "en": "Run Batch AI Translation (Cloud API)",
        "ko": "일괄 AI 번역 실행 (클라우드 API)",
        "zh-CN": "执行批量AI翻译 (云端API)",
        "es": "Ejecutar Traducción AI (API Cloud)",
    },
    "btn_translate_ollama": {
        "ja": "一括AI翻訳を実行 (Ollama)",
        "en": "Run Batch AI Translation (Ollama)",
        "ko": "일괄 AI 번역 실행 (Ollama)",
        "zh-CN": "执行批量AI翻译 (Ollama)",
        "es": "Ejecutar Traducción AI (Ollama)",
    },
    "btn_stop": {
        "ja": "⏹️ 中断 (停止)",
        "en": "⏹️ Stop",
        "ko": "⏹️ 중지",
        "zh-CN": "⏹️ 停止",
        "es": "⏹️ Detener",
    },
    "btn_apply_local": {
        "ja": "✨ ローカルMOD適用 (Zomboid/mods)",
        "en": "✨ Apply Local MOD (Zomboid/mods)",
        "ko": "✨ 로컬 모드 적용 (Zomboid/mods)",
        "zh-CN": "✨ 应用本地MOD (Zomboid/mods)",
        "es": "✨ Aplicar MOD Local (Zomboid/mods)",
    },
    "btn_export_zip": {
        "ja": "配布用ZIPエクスポート",
        "en": "Export Release ZIP",
        "ko": "배포용 ZIP 내보내기",
        "zh-CN": "导出发布用 ZIP",
        "es": "Exportar ZIP de Distribución",
    },
    "status_ready": {
        "ja": "準備完了",
        "en": "Ready",
        "ko": "준비 완료",
        "zh-CN": "就绪",
        "es": "Listo",
    },
    "sec_lang_settings": {
        "ja": "言語設定 (Language Settings)",
        "en": "Language Settings",
        "ko": "언어 설정 (Language Settings)",
        "zh-CN": "语言设置 (Language Settings)",
        "es": "Ajustes de Idioma (Language Settings)",
    },
    "lbl_ui_lang": {
        "ja": "アプリ表示言語 (UI Language):",
        "en": "App Interface Language:",
        "ko": "앱 UI 표시 언어:",
        "zh-CN": "应用界面语言 (UI Language):",
        "es": "Idioma de la Interfaz (UI):",
    },
    "lbl_target_lang": {
        "ja": "MOD翻訳先言語 (Target Language):",
        "en": "Target MOD Language:",
        "ko": "모드 번역 대상 언어:",
        "zh-CN": "MOD 目标翻译语言:",
        "es": "Idioma de Destino del MOD:",
    },
    "note_target_lang": {
        "ja": "※ 翻訳先言語を変更すると、ゲーム本体から対応する公式対訳辞書が自動ロードされます。",
        "en": "* Changing target language will automatically load official vanilla dictionary from the game.",
        "ko": "* 번역 대상 언어를 변경하면 게임 본체의 공식 대역 사전이 자동으로 로드됩니다.",
        "zh-CN": "* 更改目标语言将自动从游戏本体加载对应的官方对照词典。",
        "es": "* Cambiar el idioma de destino cargará automáticamente el diccionario oficial del juego.",
    },
    "sec_engine_settings": {
        "ja": "翻訳エンジンを選択してください",
        "en": "Select Translation Engine",
        "ko": "번역 엔진을 선택하세요",
        "zh-CN": "请选择翻译引擎",
        "es": "Selecciona el Motor de Traducción",
    },
    "rb_smart_dict": {
        "ja": "内蔵スマート辞書 (完全オフライン / 超高速)",
        "en": "Built-in Smart Dictionary (Fully Offline / Instant)",
        "ko": "내장 스마트 사전 (완전 오프라인 / 초고속)",
        "zh-CN": "内建智能词典 (完全离线 / 超高速)",
        "es": "Diccionario Inteligente Integrado (Sin Conexión / Instantáneo)",
    },
    "desc_smart_dict": {
        "ja": "公式バニラ対訳 35,000語＋定型ルール。GPU・APIキー不要で即動作。",
        "en": "Official vanilla pairs + specialized UI rules. Zero GPU or API key required.",
        "ko": "공식 바닐라 대역 35,000단어 + 정형 규칙. GPU나 API 키 없이 즉시 작동.",
        "zh-CN": "官方原版对照词典 + 专门UI规则。无需 GPU 或 API 密钥即可即刻运行。",
        "es": "Pares oficiales del juego + reglas UI. No requiere GPU ni claves API.",
    },
    "rb_ollama": {
        "ja": "Ollama ローカルLLM (完全プライベート / GPU推奨)",
        "en": "Ollama Local LLM (Fully Private / GPU Recommended)",
        "ko": "Ollama 로컬 LLM (완전한 비공개 / GPU 권장)",
        "zh-CN": "Ollama 本地LLM (完全私密 / 推荐GPU)",
        "es": "Ollama LLM Local (Privado / GPU Recomendada)",
    },
    "rb_cloud_api": {
        "ja": "クラウド AI API (GPU不要 / 最高品質 / 超高速)",
        "en": "Cloud AI API (No GPU Needed / Highest Quality / Fast)",
        "ko": "클라우드 AI API (GPU 불필요 / 최고 품질 / 초고속)",
        "zh-CN": "云端 AI API (无需GPU / 最高质量 / 极速)",
        "es": "API de IA en la Nube (Sin GPU / Máxima Calidad / Rápido)",
    },
    "btn_save_settings": {
        "ja": "💾 設定を保存",
        "en": "💾 Save Settings",
        "ko": "💾 설정 저장",
        "zh-CN": "💾 保存设置",
        "es": "💾 Guardar Ajustes",
    },
    "btn_cancel": {
        "ja": "キャンセル",
        "en": "Cancel",
        "ko": "취소",
        "zh-CN": "取消",
        "es": "Cancelar",
    },
    "msg_settings_saved": {
        "ja": "翻訳設定を保存しました！",
        "en": "Translation settings saved successfully!",
        "ko": "번역 설정이 저장되었습니다!",
        "zh-CN": "翻译设置已保存！",
        "es": "¡Ajustes de traducción guardados con éxito!",
    },
    "msg_apply_success": {
        "ja": "翻訳パッチMODをローカルに適用しました！",
        "en": "Translation patch MOD applied locally!",
        "ko": "번역 패치 모드가 로컬에 적용되었습니다!",
        "zh-CN": "翻译补丁MOD已成功应用到本地！",
        "es": "¡Parche de traducción aplicado localmente!",
    },
    "msg_export_success": {
        "ja": "配布用ZIPを作成しました！",
        "en": "Release ZIP created successfully!",
        "ko": "배포용 ZIP이 성공적으로 생성되었습니다!",
        "zh-CN": "发布用 ZIP 已成功创建！",
        "es": "¡ZIP de distribución creado con éxito!",
    },
    "msg_no_mod_selected": {
        "ja": "MODを選択してください。",
        "en": "Please select a MOD first.",
        "ko": "먼저 모드를 선택하세요.",
        "zh-CN": "请先选择一个 MOD。",
        "es": "Por favor, selecciona un MOD primero.",
    },
    "msg_no_trans_items": {
        "ja": "適用できる訳文がありません。先に翻訳を実行してください。",
        "en": "No translated items available. Please run translation first.",
        "ko": "적용할 수 있는 번역 내용이 없습니다. 먼저 번역을 실행하세요.",
        "zh-CN": "没有可应用的译文。请先执行翻译。",
        "es": "No hay elementos traducidos. Por favor ejecuta la traducción primero.",
    },
    "quickstart_title": {
        "ja": "🚀 かんたん初期セットアップ",
        "en": "🚀 Quick Start Setup",
        "ko": "🚀 빠른 초기 설정",
        "zh-CN": "🚀 快速初始设置",
        "es": "🚀 Configuración Rápida",
    },
    "quickstart_sub": {
        "ja": "MODの翻訳方法を選んでください。選択するとすぐに翻訳できます。",
        "en": "Choose your translation method. Ready to translate immediately.",
        "ko": "번역 방식을 선택하세요. 선택 후 바로 번역할 수 있습니다.",
        "zh-CN": "请选择翻译方式。选择后即可立即翻译。",
        "es": "Elige tu método de traducción. Listo para traducir de inmediato.",
    },
    "btn_quickstart": {
        "ja": "🚀 かんたん設定",
        "en": "🚀 Quick Setup",
        "ko": "🚀 빠른 설정",
        "zh-CN": "🚀 快速设置",
        "es": "🚀 Config. Rápida",
    },
    "disclaimer_title": {
        "ja": "⚖️ 免責事項・ご利用にあたって",
        "en": "⚖️ Disclaimer & Terms of Use",
        "ko": "⚖️ 면책 조항 및 이용 안내",
        "zh-CN": "⚖️ 免责声明与使用条款",
        "es": "⚖️ Descargo de Responsabilidad y Términos",
    },
    "disclaimer_sub": {
        "ja": "本ツールをご利用いただく前に、以下の内容をご確認・同意の上ご使用ください。",
        "en": "Please review and agree to the following terms before using this tool.",
        "ko": "이 도구를 사용하기 전에 다음 내용을 확인하고 동의해 주세요.",
        "zh-CN": "在使用本工具之前，请先阅读并同意以下条款。",
        "es": "Por favor, revise y acepte los siguientes términos antes de usar esta herramienta.",
    },
    "disclaimer_item1_title": {
        "ja": "非公式ファンツール",
        "en": "Unofficial Fan Tool",
        "ko": "비공식 팬 도구",
        "zh-CN": "非官方粉丝工具",
        "es": "Herramienta Fan No Oficial",
    },
    "disclaimer_item1_desc": {
        "ja": "本ソフトウェアは The Indie Stone 公式とは無関係の、ファン有志によるコミュニティ開発ツールです。",
        "en": "This software is an unofficial community project and not affiliated with or endorsed by The Indie Stone.",
        "ko": "본 소프트웨어는 The Indie Stone 공식과 무관한 커뮤니티 팬 개발 도구입니다.",
        "zh-CN": "本软件为粉丝社区开发的非官方工具，与 The Indie Stone 官方无关。",
        "es": "Este software es un proyecto no oficial de la comunidad y no está afiliado a The Indie Stone.",
    },
    "disclaimer_item2_title": {
        "ja": "原作者の権利・配布マナーの遵守",
        "en": "Respect for Original Authors & Rights",
        "ko": "원작자 권리 및 배포 가이드라인 준수",
        "zh-CN": "尊重原作者权利与发布规范",
        "es": "Respeto a los Derechos de los Autores Originales",
    },
    "disclaimer_item2_desc": {
        "ja": "生成された翻訳パッチMODをSteam Workshop等に公開する際は、必ず原作者の規約に従い、クレジット表記や事前確認を行ってください。",
        "en": "When publishing translated patch mods to the Steam Workshop, always respect the original author's policies and provide clear attribution.",
        "ko": "번역 패치 모드를 Steam 창작마당 등에 배포할 때는 반드시 원작자의 규정을 준수하고 크레딧을 명시하세요.",
        "zh-CN": "将翻译补丁 MOD 发布至 Steam 创意工坊等平台时，请务必遵守原作者的规范并注明原作者署名。",
        "es": "Al publicar mods de traducción en Steam Workshop, respete siempre las políticas del autor original y dé el crédito correspondiente.",
    },
    "disclaimer_item3_title": {
        "ja": "機械翻訳の精度と手動校正",
        "en": "AI & Machine Translation Accuracy",
        "ko": "기계 번역 정확도 및 수동 검수",
        "zh-CN": "机器翻译准确性与人工校对",
        "es": "Precisión de la Traducción Automática / IA",
    },
    "disclaimer_item3_desc": {
        "ja": "AIや内蔵辞書による翻訳結果の完全性・正確性を保証するものではありません。必要に応じて一覧画面で手動修正を行ってください。",
        "en": "Translations generated by AI or dictionaries are not guaranteed to be 100% accurate. Please review and edit manually as needed.",
        "ko": "AI 또는 내장 사전 번역 결과의 정확성을 보장하지 않습니다. 필요에 따라 목록에서 직접 수동 수정해 주세요.",
        "zh-CN": "AI 或内置字典生成的翻译结果不保证百分之百准确。请根据需要在列表中进行手动检查和修正。",
        "es": "No se garantiza la exactitud absoluta de las traducciones generadas por IA o diccionario. Revise y edite manualmente si es necesario.",
    },
    "disclaimer_item4_title": {
        "ja": "免責事項 (自己責任)",
        "en": "Disclaimer of Liability",
        "ko": "면책 조항 (사용자 책임)",
        "zh-CN": "免责声明 (自行承担风险)",
        "es": "Exención de Responsabilidad",
    },
    "disclaimer_item4_desc": {
        "ja": "本ツールの使用によって生じたゲームデータの破損、不具合、その他の損害・トラブルについて、開発者は一切の責任を負いません。",
        "en": "The developer accepts no liability for any game data corruption, conflicts, or damages arising from the use of this software.",
        "ko": "본 도구 사용으로 발생한 게임 데이터 손상, 충돌 또는 기타 문제에 대해 개발자는 어떠한 책임도 지지 않습니다.",
        "zh-CN": "对于因使用本工具导致的存档损坏、游戏崩溃或其他纠纷，开发者概不承担任何责任。",
        "es": "El desarrollador no se hace responsable de daños a partidas guardadas, conflictos o inconvenientes derivados del uso de esta herramienta.",
    },
    "disclaimer_dont_show": {
        "ja": "次回からこの免責事項を表示しない",
        "en": "Do not show this disclaimer again",
        "ko": "다음부터 이 면책 조항을 표시하지 않음",
        "zh-CN": "下次不再显示此免责声明",
        "es": "No volver a mostrar este aviso",
    },
    "disclaimer_btn_agree": {
        "ja": "同意して進む",
        "en": "Agree & Continue",
        "ko": "동의하고 계속하기",
        "zh-CN": "同意并继续",
        "es": "Aceptar y Continuar",
    },
    "btn_disclaimer": {
        "ja": "⚖ 免責事項",
        "en": "⚖ Disclaimer",
        "ko": "⚖ 면책 조항",
        "zh-CN": "⚖ 免责声明",
        "es": "⚖ Aviso legal",
    },
}

_CURRENT_LANG = "ja"


def set_ui_language(lang_code: str):
    global _CURRENT_LANG
    if lang_code in SUPPORTED_UI_LANGUAGES:
        _CURRENT_LANG = lang_code


def get_ui_language() -> str:
    return _CURRENT_LANG


def t(key: str, **kwargs) -> str:
    """翻訳キーから現在のUI言語の文言を取得"""
    entry = STRINGS.get(key, {})
    text = entry.get(_CURRENT_LANG) or entry.get("ja") or entry.get("en") or key
    if kwargs:
        try:
            text = text.format(**kwargs)
        except Exception:
            pass
    return text

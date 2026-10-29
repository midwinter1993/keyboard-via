import json
import copy

INPUT_FILE = "keyboard.vil"
OUTPUT_FILE = "keyboard-mac-win.vil"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# 保留原始 Layer 0 和 Layer 1，用来建立 Windows / Fn 层。
original_layer0 = copy.deepcopy(data["layout"][0])
original_layer1 = copy.deepcopy(data["layout"][1])

# ============================================================
# Layer 0：Mac 基础层
# ============================================================
mac_base = copy.deepcopy(original_layer0)

# 底行索引：
# [0] Ctrl, [1] Win, [2] Alt, [3] Space, [4] Fn,
# [5] Space, [6] 空, [7] Space, [8] 空,
# [9] Right Alt, [10] Menu, [11] 空, [12] Fn, [13] Right Ctrl

# 左侧 Mac 修饰键：
mac_base[4][0] = "KC_LCTRL"
mac_base[4][1] = "KC_LALT"   # 物理 Win → Mac Option
mac_base[4][2] = "KC_LGUI"   # 物理 Alt → Mac Command

# 三个空格：轻按空格，按住进入 Mac Fn 层（Layer 1）
mac_base[4][3] = "LT(1,KC_SPACE)"
mac_base[4][5] = "LT(1,KC_SPACE)"
mac_base[4][7] = "LT(1,KC_SPACE)"

# 两个物理 Fn 键进入 Mac Fn 层
mac_base[4][4] = "MO(1)"
mac_base[4][12] = "MO(1)"

# 右侧修饰键按 Mac 习惯调整：
# 空格右侧最近的键为 Command，外侧为 Option。
mac_base[4][9] = "KC_RGUI"
mac_base[4][10] = "KC_RALT"
mac_base[4][13] = "KC_RCTRL"

# ============================================================
# Layer 1：Mac Fn + RGB 灯光 + 导航层
# ============================================================
mac_fn = copy.deepcopy(original_layer1)

# ----------------------------
# 导航键：H/J/K/L = 方向键
# ----------------------------
mac_fn[2][6] = "KC_LEFT"   # H
mac_fn[2][7] = "KC_DOWN"   # J
mac_fn[2][8] = "KC_UP"     # K
mac_fn[2][9] = "KC_RIGHT"  # L

# ----------------------------
# 导航键：U/I/O/P/Y/B = Home/`/End/~/PgUp/PgDn
# ----------------------------
mac_fn[1][7] = "KC_HOME"   # U
mac_fn[1][8] = "LSFT(KC_GRV)" # I → ~
mac_fn[1][9] = "KC_END"    # O
mac_fn[1][10] = "KC_GRV"   # P → 反引号 `
mac_fn[1][6] = "KC_PGUP"   # Y → Page Up
mac_fn[3][5] = "KC_PGDN"   # B → Page Down
mac_fn[3][8] = "KC_VOLD"   # , → Volume Down
mac_fn[3][9] = "KC_VOLU"   # . → Volume Up
mac_fn[1][1] = "LGUI(KC_GRV)" # Q → Cmd+` 切换窗口
mac_fn[2][4] = "LALT(KC_F)"   # F → Alt/Option+F（zellij floating panel）

# M：将 Windows Layer 2 设为默认层
mac_fn[3][7] = "DF(2)"

# ----------------------------
# 功能键调整
# ----------------------------
# Esc：不再进入 Bootloader，恢复为 Escape
mac_fn[0][0] = "KC_ESCAPE"
# Backspace：Delete
mac_fn[0][13] = "KC_DELETE"
# \：Bootloader
mac_fn[1][13] = "QK_BOOT"

# ============================================================
# Layer 2：Windows 基础层
# ============================================================
win_base = copy.deepcopy(original_layer0)

# Windows 左侧修饰键
win_base[4][0] = "KC_LCTRL"
win_base[4][1] = "KC_LGUI"
win_base[4][2] = "KC_LALT"

# 三个空格：轻按空格，按住进入 Windows Fn 层（Layer 3）
win_base[4][3] = "LT(3,KC_SPACE)"
win_base[4][5] = "LT(3,KC_SPACE)"
win_base[4][7] = "LT(3,KC_SPACE)"

# 两个物理 Fn 键进入 Windows Fn 层
win_base[4][4] = "MO(3)"
win_base[4][12] = "MO(3)"

# Windows 右侧修饰键
win_base[4][9] = "KC_RALT"
win_base[4][10] = "KC_APPLICATION"
win_base[4][13] = "KC_RCTRL"

# ============================================================
# Layer 3：Windows Fn + RGB 灯光 + 导航层
# ============================================================
win_fn = copy.deepcopy(original_layer1)

# ----------------------------
# 导航键：H/J/K/L = 方向键
# ----------------------------
win_fn[2][6] = "KC_LEFT"   # H
win_fn[2][7] = "KC_DOWN"   # J
win_fn[2][8] = "KC_UP"     # K
win_fn[2][9] = "KC_RIGHT"  # L

# ----------------------------
# 导航键：U/I/O/P/Y/B = Home/`/End/~/PgUp/PgDn
# ----------------------------
win_fn[1][7] = "KC_HOME"   # U
win_fn[1][8] = "LSFT(KC_GRV)" # I → ~
win_fn[1][9] = "KC_END"    # O
win_fn[1][10] = "KC_GRV"   # P → 反引号 `
win_fn[1][6] = "KC_PGUP"   # Y → Page Up
win_fn[3][5] = "KC_PGDN"   # B → Page Down
win_fn[3][8] = "KC_VOLD"   # , → Volume Down
win_fn[3][9] = "KC_VOLU"   # . → Volume Up
win_fn[2][4] = "LALT(KC_F)" # F → Alt/Option+F（zellij floating panel）

# M：将 Mac Layer 0 设为默认层
win_fn[3][7] = "DF(0)"

# ----------------------------
# 功能键调整
# ----------------------------
# Esc：不再进入 Bootloader，恢复为 Escape
win_fn[0][0] = "KC_ESCAPE"
# Backspace：Delete
win_fn[0][13] = "KC_DELETE"
# \：Bootloader
win_fn[1][13] = "QK_BOOT"

# ============================================================
# 写入四层
# ============================================================
data["layout"][0] = mac_base
data["layout"][1] = mac_fn
data["layout"][2] = win_base
data["layout"][3] = win_fn

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

print(f"已生成：{OUTPUT_FILE}")
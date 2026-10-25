# -*- coding: utf-8 -*-
"""
一键把网页版重新打成 Android APK。

流程：
  1. 跑 build.py 生成最新的 信息科技_汇总刷题.html
  2. 同步到工程 assets 的 web 源目录
  3. 调 html-to-apk skill 的 build_apk.py 完成 aapt2/javac/d8/签名
  4. 把产物复制回 整合/ 目录

用法：python build_apk.py            （版本号不变，重打当前版）
      python build_apk.py --v 2.0    （同时改版本名，需先改 AndroidManifest 的 versionCode）

注意：Android 工程必须放在**纯英文路径**下（aapt2 读不了中文目录），
      当前工程在 C:\\Users\\<用户>\\apkbuild\\xxkj_apk。
"""
import os, sys, shutil, subprocess, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
INTEG = os.path.dirname(HERE)                      # 整合/
ROOT = os.path.dirname(INTEG)                      # 信息科技/
PROJ = os.path.join(os.path.expanduser("~"), "apkbuild", "xxkj_apk")
SKILL = os.path.join(os.path.expanduser("~"), ".workbuddy", "skills", "html-to-apk", "scripts")
PY = sys.executable

HTML = os.path.join(INTEG, "信息科技_汇总刷题.html")
WEB = os.path.join(PROJ, "web", "index.html")


def run(args, label):
    print("[%s] %s" % (label, os.path.basename(args[1]) if len(args) > 1 else ""))
    r = subprocess.run(args, capture_output=True)
    out = (r.stdout or b"").decode("utf-8", "replace")
    err = (r.stderr or b"").decode("utf-8", "replace")
    if r.returncode != 0:
        print(out[-3000:])
        print(err[-3000:])
        raise SystemExit("%s 失败（exit %d）" % (label, r.returncode))
    return out


def main():
    if not os.path.isdir(PROJ):
        raise SystemExit("找不到 Android 工程：%s\n请先用 new_project.py 生成" % PROJ)
    if not os.path.isfile(os.path.join(SKILL, "build_apk.py")):
        raise SystemExit("找不到 html-to-apk skill：%s" % SKILL)

    # 1. 生成网页
    run([PY, os.path.join(HERE, "build.py")], "1/4 生成网页")
    print("    " + HTML)

    # 2. 同步到工程
    os.makedirs(os.path.dirname(WEB), exist_ok=True)
    shutil.copy2(HTML, WEB)
    print("[2/4] 已同步 index.html  %.2f MB" % (os.path.getsize(WEB) / 1024 / 1024))

    # 3. 版本号
    mf = os.path.join(PROJ, "AndroidManifest.xml")
    src = open(mf, encoding="utf-8").read()
    ver = re.search(r'android:versionName="([^"]+)"', src).group(1)
    if "--v" in sys.argv:
        newv = sys.argv[sys.argv.index("--v") + 1]
        code = int(re.search(r'android:versionCode="(\d+)"', src).group(1)) + 1
        src = re.sub(r'android:versionName="[^"]+"', 'android:versionName="%s"' % newv, src)
        src = re.sub(r'android:versionCode="\d+"', 'android:versionCode="%d"' % code, src)
        open(mf, "w", encoding="utf-8").write(src)
        ver = newv
        print("[3/4] 版本号改为 %s（versionCode=%d）" % (ver, code))
    else:
        print("[3/4] 版本号 %s（不变）" % ver)

    # 4. 打包
    name = "信息科技题库-v%s.apk" % ver
    run([PY, os.path.join(SKILL, "build_apk.py"),
         "--project", PROJ, "--web", os.path.join(PROJ, "web"),
         "--name", name], "4/4 打包 APK")

    apk = os.path.join(PROJ, "dist", name)
    if not os.path.isfile(apk):
        raise SystemExit("没有找到产物：" + apk)
    dst = os.path.join(INTEG, name)
    shutil.copy2(apk, dst)
    print("\n完成：%s" % dst)
    print("体积：%.2f MB" % (os.path.getsize(dst) / 1024 / 1024))


if __name__ == "__main__":
    main()

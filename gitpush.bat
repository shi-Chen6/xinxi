@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ============================================
echo   信息科技项目 - 一键推送到 GitHub
echo   仓库: git@github.com:shi-Chen6/xinxi.git
echo ============================================
echo.

echo [1/3] 正在暂存改动...
git add -A

echo [2/3] 正在提交...
git commit -m "update: sync teaching resources"
if errorlevel 1 echo     (没有新改动，跳过提交)

echo [3/3] 正在推送...
git push origin main

echo.
if errorlevel 1 (
    echo [失败] 推送出错，请检查网络或 SSH 密钥
) else (
    echo [成功] 已同步到 https://github.com/shi-Chen6/xinxi
)
echo.
echo 按任意键关闭窗口...
pause >nul

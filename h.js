const robot = require('robotjs');
const screenshot = require('screenshot-desktop');
const fs = require('fs');
const { match } = require('@nut-tree/nut-js'); // 用于图像匹配

// 等待几秒以切换到微信小程序界面
console.log("脚本开始运行，请在5秒内切换到微信小程序界面");
setTimeout(() => {
    // 定义K值，控制循环次数
    let K = 0;

    // 设置置信度阈值（可选，根据实际情况调整）
    const confidence_threshold = 0.8; // 图片相似度

    // 获取当前屏幕分辨率
    const screen = robot.getScreenSize();
    const screen_width = screen.width;
    const screen_height = screen.height;
    console.log(`屏幕分辨率: ${screen_width}x${screen_height}`);

    // 大循环
    const loop = async () => {
        while (K < 5) {
            try {
                // 尝试找到开始图像
                const startlocation = await findImageOnScreen('start.png', confidence_threshold);
                if (startlocation) {
                    console.log("图像找到，位置：", startlocation);
                    // 如果识别到start图片，点击其中心位置
                    const start_center = {
                        x: startlocation.x + startlocation.width / 2,
                        y: startlocation.y + startlocation.height / 2
                    };
                    robot.moveMouse(start_center.x, start_center.y);
                    robot.mouseClick();
                    K++;
                    console.log("开始第" + K + "局");
                    await sleep(15000);
                } else {
                    console.log("图像未找到");
                }
            } catch (e) {
                console.log("其他错误：", e);
            }

            try {
                // 尝试找到继续图像
                const continuelocation = await findImageOnScreen('continue.png', confidence_threshold);
                if (continuelocation) {
                    console.log("图像找到，位置：", continuelocation);
                    // 如果识别到continue图片，点击其中心位置
                    const continue_center = {
                        x: continuelocation.x + continuelocation.width / 2,
                        y: continuelocation.y + continuelocation.height / 2
                    };
                    robot.moveMouse(continue_center.x, continue_center.y);
                    robot.mouseClick();
                    console.log("点击继续");
                    // await sleep(2000);
                } else {
                    console.log("图像未找到");
                }
            } catch (e) {
                console.log("其他错误：", e);
            }

            try {
                // 尝试找到退出图像
                const endlocation = await findImageOnScreen('end.png', confidence_threshold);
                if (endlocation) {
                    console.log("图像找到，位置：", endlocation);
                    // 如果识别到continue图片，点击其中心位置
                    const end_center = {
                        x: endlocation.x + endlocation.width / 2,
                        y: endlocation.y + endlocation.height / 2
                    };
                    robot.moveMouse(end_center.x, end_center.y);
                    robot.mouseClick();
                    console.log("退出对局");
                    // await sleep(2000);
                } else {
                    console.log("图像未找到");
                }
            } catch (e) {
                console.log("其他错误：", e);
            }

            for (let i = 0; i < 1; i++) {
                const x = 700;
                const y = 900;
                robot.moveMouse(x, y);
                robot.mouseToggle(true);
                robot.moveMouse(x - 100, y, 600);
                robot.moveMouse(x - 100, y - 100, 600);
                robot.moveMouse(x, y - 100, 600);
                robot.moveMouse(x, y, 600);
                robot.mouseToggle(false);
                console.log("控制移动");

                // 点击屏幕右侧
                robot.moveMouse(1500, 900);
                robot.mouseClick();
                robot.mouseClick();
                robot.mouseClick();
                console.log("控制开火");

                // 每次操作后等待6秒
                await sleep(6000);
            }
        }
        console.log("脚本执行完毕");
    };

    loop();
}, 5000);

// 辅助函数：找到图像在屏幕上的位置
async function findImageOnScreen(imagePath, confidence) {
    const imgBuffer = fs.readFileSync(imagePath);
    const screenBuffer = await screenshot();
    const result = await match(imgBuffer, screenBuffer, { confidence });
    if (result.matches.length > 0) {
        const match = result.matches[0];
        return {
            x: match.x,
            y: match.y,
            width: match.width,
            height: match.height
        };
    }
    return null;
}

// 辅助函数：睡眠函数
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
document.onreadystatechange = function () {
    if (document.readyState == "complete") {
        var game = new PixelJS.Engine();
        game.init({
            container: 'game_container',
            width: 800,
            height: 600
        });
        
        game.run(function (elapsedTime, dt) {
        });

        var backgroundLayer = game.createLayer('background');
        var grass = backgroundLayer.createEntity();
        backgroundLayer.static = true;
        grass.pos = { x: 0, y: 0 };
        grass.asset = new PixelJS.Tile();
        grass.asset.prepare({
            name: 'grass.png',
            size: { 
                width: 800, 
                height: 600 
            }
        });
        PixelJS.assetPath = '/static/assets';

        var playerLayer = game.createLayer("players");
        var player = new PixelJS.Player();
        player.addToLayer(playerLayer);
        player.pos = { x: 200, y: 300 };
        player.size = { width: 32, height: 32 };
        player.velocity = { x: 100, y: 100 };
        player.asset = new PixelJS.AnimatedSprite();
        player.asset.prepare({ 
            name: 'char.png', 
            frames: 3, 
            rows: 4,
            speed: 100,
            defaultFrame: 1
        });
    }
}
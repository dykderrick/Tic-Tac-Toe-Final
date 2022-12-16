const statusDisplay = document.querySelector('.game--status');

let gameActive = true;
let currentPlayer = "X";
let gameState = ["", "", "", "", "", "", "", "", ""];

const winningMessage = () => `Player ${currentPlayer} has won!`;
const drawMessage = () => `Game ended in a draw!`;
const currentPlayerTurn = () => `It's ${currentPlayer}'s turn`;

let game_mode = document.getElementById("game_mode_variable").innerHTML.replace(/\s+/g,'');
let player_1_name = document.getElementById("player_1_name_variable").innerHTML.replace(/\s+/g,'');
let player_2_name = document.getElementById("player_2_name_variable").innerHTML.replace(/\s+/g,'');

let isSingleModeGame = game_mode === 'SingleMode';

statusDisplay.innerHTML = currentPlayerTurn();

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

function handleCellPlayed(clickedCell, clickedCellIndex) {
    gameState[clickedCellIndex] = currentPlayer;
    clickedCell.innerHTML = currentPlayer;
}

function getBotRandomStepCellId() {
    let freeCellIds = [];

    gameState.forEach(function (value, index) {
        if (value === "") {
            freeCellIds.push(index);
        }
    });

    return 'cell' + freeCellIds[Math.floor(Math.random() * freeCellIds.length)].toString()

}

function handlePlayerChange() {
    if (gameActive) {
        currentPlayer = currentPlayer === "X" ? "O" : "X";
    }

    if (isSingleModeGame && currentPlayer === "O") {  // BOT step
        document.getElementById(getBotRandomStepCellId()).click();

        handleResultValidation();

        // Toggle Player
        if (gameActive) {
            currentPlayer = 'X';
        }
    }

    if (gameActive) {
        statusDisplay.innerHTML = currentPlayerTurn();
    }
}

function handleResultValidation() {
    let roundWon = false;
    for (let i = 0; i <= 7; i++) {
        const winCondition = winningConditions[i];
        let a = gameState[winCondition[0]];
        let b = gameState[winCondition[1]];
        let c = gameState[winCondition[2]];
        if (a === '' || b === '' || c === '') {
            continue;
        }
        if (a === b && b === c) {
            roundWon = true;
            break
        }
    }

    if (roundWon) {
        statusDisplay.innerHTML = winningMessage();
        gameActive = false;
        return;
    }

    let roundDraw = !gameState.includes("");
    if (roundDraw) {
        statusDisplay.innerHTML = drawMessage();
        gameActive = false;
        return;
    }
}

function handleCellClick(clickedCellEvent) {
    const clickedCell = clickedCellEvent.target;
    const clickedCellIndex = parseInt(clickedCell.getAttribute('data-cell-index'));

    if (gameState[clickedCellIndex] !== "" || !gameActive) {
        return;
    }

    handleCellPlayed(clickedCell, clickedCellIndex);
    handleResultValidation();
    handlePlayerChange();
}

function handleRestartGame() {
    gameActive = true;
    currentPlayer = "X";
    gameState = ["", "", "", "", "", "", "", "", ""];
    statusDisplay.innerHTML = currentPlayerTurn();
    document.querySelectorAll('.cell').forEach(cell => cell.innerHTML = "");
}

document.querySelectorAll('.cell').forEach(cell => cell.addEventListener('click', handleCellClick));
document.querySelector('.game--restart').addEventListener('click', handleRestartGame);
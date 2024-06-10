const content = await Bun.file("./src/input.secret").text().then(t => t.trim().split("\n"))


type Color = "red" | "green" | "blue"

function parse_line(line: string): { id: number, items: Record<string, number>[] } {
    const [game, items] = line.split(":")
    const game_id = Number.parseInt(game.trim().split(" ")[1])

    const item_list = items.split(";")
        .map(item => {
            const values = item
            .trim()
            .split(",")
            .map(selection => selection
                .trim()
                .split(" ")
                .toReversed()
            ) as [Color, string][]

            const ret: Record<Color, number> = { red: 0, green: 0, blue: 0 }
            values.forEach(([key, value]) => ret[key] = Number.parseInt(value))

            return ret
        })

    return { id: game_id, items: item_list }
}

const games = content.map(parse_line)

const max_items = { red: 12, green: 13, blue: 14 }
const is_valid = (items: Record<string, number>[]) => items.reduce<boolean>((acc, item) => acc && (
    item.red <= max_items.red &&
    item.green <= max_items.green &&
    item.blue <= max_items.blue
), true)

const answer_1 = games
    .map(({ id, items }) => ({id, valid: is_valid(items)}))
    .filter(({ valid }) => valid)
    .reduce((acc, { id }) => acc + id, 0)

console.log(`Answer 1: ${answer_1}`)

const get_min = (items: Record<string, number>[], color: Color) => items.reduce((acc, item) => Math.min(acc, item[color]), items[0][color])

const answer_2 = games
    .map(({ items }) => get_min(items, "red") * get_min(items, "green") * get_min(items, "blue"))
    .reduce((acc, power) => acc + power, 0)

console.log(`Answer 2: ${answer_2}`)
from manim import *
import random


class ThanosSort(Scene):

    def construct(self):

        # =========================================================
        # DATA
        # =========================================================

        values = [
            7, 3, 12, 1, 9,
            4, 15, 2, 11, 6,
            14, 5, 10, 8, 13
        ]

        # =========================================================
        # TITLE
        # =========================================================

        title = Text(
            "THANOS SORT",
            font_size=48,
            weight=BOLD
        )

        subtitle = Text(
            "Perfectly balanced... as all things should be.",
            font_size=22
        )

        title.to_edge(UP)
        subtitle.next_to(title, DOWN, buff=0.15)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)

        # =========================================================
        # CREATE INITIAL ARRAY
        # =========================================================

        boxes = VGroup()
        labels = VGroup()

        spacing = 0.93

        start_x = -(len(values) - 1) * spacing / 2

        for i, value in enumerate(values):

            box = Square(
                side_length=0.75,
                stroke_width=2
            )

            box.move_to(
                RIGHT * (start_x + i * spacing)
                + DOWN * 0.5
            )

            label = Text(
                str(value),
                font_size=25
            )

            label.move_to(box.get_center())

            boxes.add(box)
            labels.add(label)

        self.play(
            LaggedStart(
                *[
                    FadeIn(box, scale=0.7)
                    for box in boxes
                ],
                lag_ratio=0.05
            )
        )

        self.play(
            LaggedStart(
                *[
                    Write(label)
                    for label in labels
                ],
                lag_ratio=0.05
            )
        )

        self.wait(1)

        # =========================================================
        # HELPER FUNCTIONS
        # =========================================================

        def is_sorted(arr):

            return all(
                arr[i] <= arr[i + 1]
                for i in range(len(arr) - 1)
            )

        def create_status(text):

            return Text(
                text,
                font_size=27
            ).to_edge(DOWN)

        # =========================================================
        # CURRENT ARRAY
        # =========================================================

        current_values = values.copy()
        current_boxes = boxes
        current_labels = labels

        generation = 0

        # =========================================================
        # THANOS SORT
        # =========================================================

        while not is_sorted(current_values):

            generation += 1

            # -----------------------------------------------------
            # STATUS
            # -----------------------------------------------------

            status = create_status(
                "Array is NOT sorted — Thanos must intervene."
            )

            self.play(FadeIn(status))
            self.wait(0.5)

            # -----------------------------------------------------
            # THANOS SNAP TEXT
            # -----------------------------------------------------

            thanos = Text(
                "THANOS SNAP!",
                font_size=42,
                weight=BOLD
            )

            thanos.set_color(RED)
            thanos.move_to(UP * 1.7)

            self.play(
                Write(thanos),
                run_time=0.6
            )

            # -----------------------------------------------------
            # SELECT SURVIVORS
            # -----------------------------------------------------

            count = len(current_values)

            survivors_count = max(
                1,
                count // 2
            )

            indices = list(range(count))
            random.shuffle(indices)

            survivor_indices = sorted(
                indices[:survivors_count]
            )

            removed_indices = [
                i
                for i in range(count)
                if i not in survivor_indices
            ]

            # -----------------------------------------------------
            # SNAP DELETED ELEMENTS
            # -----------------------------------------------------

            snap_anims = []

            for i in removed_indices:

                snap_anims.append(
                    current_boxes[i].animate
                    .scale(0.05)
                    .set_opacity(0)
                )

                snap_anims.append(
                    current_labels[i].animate
                    .scale(0.05)
                    .set_opacity(0)
                )

            self.play(
                *snap_anims,
                run_time=1.2
            )

            # -----------------------------------------------------
            # REMOVE DELETED OBJECTS FROM SCENE
            # -----------------------------------------------------

            for i in removed_indices:

                self.remove(current_boxes[i])
                self.remove(current_labels[i])

            # -----------------------------------------------------
            # SURVIVORS
            # -----------------------------------------------------

            survivors = [
                current_values[i]
                for i in survivor_indices
            ]

            survivor_boxes = VGroup(
                *[
                    current_boxes[i]
                    for i in survivor_indices
                ]
            )

            survivor_labels = VGroup(
                *[
                    current_labels[i]
                    for i in survivor_indices
                ]
            )

            # -----------------------------------------------------
            # REPOSITION SURVIVORS
            # -----------------------------------------------------

            new_start_x = (
                -(len(survivors) - 1)
                * spacing
                / 2
            )

            move_anims = []

            for i in range(len(survivors)):

                new_position = (
                    RIGHT
                    * (
                        new_start_x
                        + i * spacing
                    )
                    + DOWN * 0.5
                )

                move_anims.append(
                    survivor_boxes[i].animate.move_to(
                        new_position
                    )
                )

                move_anims.append(
                    survivor_labels[i].animate.move_to(
                        new_position
                    )
                )

            self.play(
                *move_anims,
                run_time=1
            )

            # -----------------------------------------------------
            # UPDATE CURRENT ARRAY
            # -----------------------------------------------------

            current_values = survivors
            current_boxes = survivor_boxes
            current_labels = survivor_labels

            # -----------------------------------------------------
            # CLEANUP TEXT
            # -----------------------------------------------------

            self.play(
                FadeOut(thanos),
                FadeOut(status)
            )

            self.wait(0.5)

        # =========================================================
        # FINAL SORTED ARRAY
        # =========================================================

        final_status = Text(
            "The universe is balanced.",
            font_size=32,
            weight=BOLD
        )

        final_status.set_color(GREEN)
        final_status.to_edge(DOWN)

        self.play(
            *[
                box.animate.set_color(GREEN)
                for box in current_boxes
            ],
            run_time=0.8
        )

        self.play(
            Write(final_status)
        )

        self.wait(2)

        # =========================================================
        # END CARD
        # =========================================================

        complexity = Text(
            "Thanos Sort: O(∞) in the worst case",
            font_size=24
        )

        complexity.next_to(
            final_status,
            UP,
            buff=0.25
        )

        self.play(
            FadeIn(complexity)
        )

        self.wait(3)

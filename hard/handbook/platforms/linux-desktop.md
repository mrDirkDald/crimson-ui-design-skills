# Linux Desktop

## Platform lens

GTK/Qt conventions, varying desktop environments, theme integration, font/rendering variability, package/runtime constraints, keyboard-first workflows.

## Design rule

Respect platform expectations unless the product has a concrete reason to diverge. “Cross-platform consistency” does not require making every platform identical. Preserve product identity while adapting interaction, navigation, typography, density, windowing, system surfaces, and accessibility to the environment.

## Verification

Test the real platform behavior whenever possible. Emulator/browser screenshots cannot prove every native convention, input behavior, system dialog, DPI issue, safe-area issue, or accessibility API mapping.

## Iconography

Preserve a coherent existing icon set. Otherwise use Lucide/vector assets where appropriate. When the platform has a strong semantic native symbol system, use it when it materially improves platform correctness, but do not mix styles randomly. Emoji are not UI icons.
